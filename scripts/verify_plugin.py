#!/usr/bin/env python3
"""Simulate plugin discovery, the way a client would resolve it.

**What this does NOT do:** run `/plugin marketplace add` or `/plugin install`. Those are
client commands and cannot be executed from a build script. This walks the same path the
loader documents — marketplace catalog → plugin source → `skills/<name>/SKILL.md` → skill
frontmatter — and reports what a client *would* discover, plus anything that would break.

A green run here means the layout and manifests are structurally correct. It is evidence,
not proof: only a real `/plugin install` proves the install. Said plainly because this repo
tells its users not to present a partial check as a clean bill of health
(`references/document-intelligence.md` §5).

Usage:  python scripts/verify_plugin.py
Exit 0 = discovery resolves. Stdlib only.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# From the published claude-code-marketplace schema.
PLUGIN_NAME_RE = re.compile(r"^[A-Za-z0-9][-A-Za-z0-9._]*$")
SKILL_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")

problems: list[str] = []
notes: list[str] = []


def ok(msg: str) -> None:
    print(f"  ok   {msg}")


def bad(msg: str) -> None:
    print(f"  FAIL {msg}")
    problems.append(msg)


def note(msg: str) -> None:
    print(f"  note {msg}")
    notes.append(msg)


def split_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[3:end]
    return ""


def main() -> int:
    print("Simulating plugin discovery (NOT running /plugin install)\n")

    mp_path = ROOT / ".claude-plugin" / "marketplace.json"
    if not mp_path.is_file():
        bad(f"no marketplace catalog at {mp_path.relative_to(ROOT).as_posix()}")
        return 1
    ok(f"marketplace catalog found at {mp_path.relative_to(ROOT).as_posix()}")

    try:
        mp = json.loads(mp_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        bad(f"marketplace.json is not valid JSON — {exc}")
        return 1

    # --- catalog level -------------------------------------------------------------
    market = mp.get("name")
    ok(f"marketplace name: {market!r}") if market else bad("marketplace has no 'name'")
    if not mp.get("owner", {}).get("name"):
        bad("marketplace has no owner.name (required)")
    entries = mp.get("plugins") or []
    if not entries:
        bad("marketplace lists no plugins")
        return 1
    ok(f"{len(entries)} plugin entr{'y' if len(entries)==1 else 'ies'} in the catalog")

    # --- per plugin ----------------------------------------------------------------
    for e in entries:
        name = e.get("name", "")
        print(f"\n  --- resolving plugin {name!r} ---")
        if not PLUGIN_NAME_RE.match(name or ""):
            bad(f"plugin name {name!r} does not match the published schema pattern")
        src_raw = e.get("source")
        if not isinstance(src_raw, str):
            note(f"{name}: non-local source ({type(src_raw).__name__}) — cannot resolve on disk")
            continue
        src = (ROOT / src_raw.lstrip("./")).resolve()
        if not src.is_dir():
            bad(f"{name}: source {src_raw!r} does not resolve to a directory")
            continue
        ok(f"source {src_raw!r} -> {src.relative_to(ROOT).as_posix()}/")

        pj = src / ".claude-plugin" / "plugin.json"
        if not pj.is_file():
            bad(f"{name}: no plugin.json under the source")
        else:
            d = json.loads(pj.read_text(encoding="utf-8"))
            ok("plugin.json present and valid JSON")
            if d.get("name") != name:
                bad(f"{name}: plugin.json name {d.get('name')!r} != catalog name {name!r}")

        # Documented default: skills load from `skills/` under the plugin source.
        skills_dir = src / "skills"
        if not skills_dir.is_dir():
            bad(f"{name}: no skills/ directory under the source — a client would find no skills")
            continue
        found = sorted(p for p in skills_dir.glob("*/SKILL.md"))
        if not found:
            bad(f"{name}: skills/ exists but contains no <skill>/SKILL.md")
            continue
        ok(f"skills/ scan discovers {len(found)} skill(s)")

        for sk in found:
            slug = sk.parent.name
            fm = split_frontmatter(sk.read_text(encoding="utf-8"))
            if not fm:
                bad(f"{slug}: SKILL.md has no YAML frontmatter — a loader would skip it")
                continue
            m = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
            declared = m.group(1) if m else None
            if not SKILL_NAME_RE.match(slug):
                bad(f"{slug}: directory name is not a valid skill slug")
            if declared and declared != slug:
                bad(f"{slug}: frontmatter name {declared!r} != directory name {slug!r}")
            if "description:" not in fm:
                bad(f"{slug}: no description — the skill would never auto-trigger")
            ok(f"discovered skill {slug!r} (namespaced as /{name}:{slug})")

    # --- double-load hazard ---------------------------------------------------------
    print()
    stray = [p for p in ROOT.glob("skills/*/SKILL.md")]
    if stray:
        bad("a top-level skills/ tree exists — cloning this repo into ~/.claude/skills/ "
            "could load the skill twice")
    else:
        ok("no top-level skills/ tree — cloning into ~/.claude/skills/ cannot double-load")

    print()
    if problems:
        print(f"FAILED: {len(problems)} problem(s)")
        return 1
    print("Discovery resolves cleanly.")
    print("NOT VERIFIED HERE: the actual `/plugin marketplace add` + `/plugin install` round-trip,")
    print("which requires an interactive Claude Code CLI session.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
