#!/usr/bin/env python3
"""Validate the Master Builder skill's structure.

CONTRIBUTING.md states the rules (keep SKILL.md lean, route to references/, every
reference listed in the table). This file *enforces* them — the skill's own
"compliance-as-code" doctrine (references/build-doctrine.md §8) applied to itself:
catch a broken skill at authoring time, not when a builder installs it.

Usage:  python scripts/validate.py
Exit 0 = valid. Stdlib only.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
REFS = ROOT / "references"

# SKILL.md must stay lean enough to be cheap to load; references carry the depth.
MAX_SKILL_LINES = 500

failures: list[str] = []
warnings: list[str] = []


def check(label: str, cond: bool, detail: str = "") -> None:
    if cond:
        print(f"  ok   {label}")
    else:
        print(f"  FAIL {label}{(': ' + detail) if detail else ''}")
        failures.append(label)


def warn(label: str, cond: bool, detail: str = "") -> None:
    if cond:
        print(f"  ok   {label}")
    else:
        print(f"  warn {label}{(': ' + detail) if detail else ''}")
        warnings.append(label)


def main() -> int:
    print("Validating the Master Builder skill")

    check("SKILL.md exists", SKILL.is_file())
    check("references/ exists", REFS.is_dir())
    if failures:
        print("\nFAILED: the skill is missing its core files.")
        return 1

    text = SKILL.read_text(encoding="utf-8")
    lines = text.splitlines()

    # --- frontmatter -------------------------------------------------------------
    check("SKILL.md starts with YAML frontmatter", text.startswith("---"))
    end = text.find("\n---", 3)
    check("frontmatter is terminated", end != -1)
    if end == -1:
        print("\nFAILED: unterminated frontmatter.")
        return 1
    fm = text[3:end]

    name_m = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    check("frontmatter declares a name", bool(name_m))
    if name_m:
        name = name_m.group(1)
        # claude.ai requires the skill name to match its folder and be slug-shaped.
        check("name is a lowercase slug (a-z, 0-9, hyphen; <=64 chars)",
              bool(re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", name)), name)
        warn("name matches the repo folder name", name == ROOT.name,
             f"name={name!r} folder={ROOT.name!r} (matters for the claude.ai uploader)")

    check("frontmatter declares a description", "description:" in fm)
    desc = " ".join(
        ln.strip() for ln in fm.split("description:", 1)[1].splitlines()[1:]
        if ln.strip() and ln[:1].isspace()
    ) if "description:" in fm else ""
    check("description is substantive (>120 chars, drives auto-triggering)",
          len(desc) > 120, f"{len(desc)} chars")

    # --- leanness / progressive disclosure ----------------------------------------
    check(f"SKILL.md stays lean (<= {MAX_SKILL_LINES} lines)",
          len(lines) <= MAX_SKILL_LINES, f"{len(lines)} lines")

    # --- reference table <-> disk --------------------------------------------------
    body = text[end + 4:]
    listed = [m.group(1) for m in re.finditer(r"\|\s*`references/([^`]+)`\s*\|", body)]
    on_disk = sorted(p.name for p in REFS.glob("*.md"))

    check("SKILL.md has a reference table", bool(listed))
    missing = [n for n in listed if n not in on_disk]
    check("every reference in the table exists on disk", not missing, ", ".join(missing))
    unlisted = [n for n in on_disk if n not in listed]
    check("every reference on disk is listed in the table", not unlisted, ", ".join(unlisted))

    # --- references are real content, with a heading and no stray frontmatter -------
    for name in on_disk:
        t = (REFS / name).read_text(encoding="utf-8")
        check(f"{name} is non-trivial and starts with a heading",
              len(t) > 500 and t.lstrip().startswith("#"), f"{len(t)} bytes")

    # --- internal cross-links resolve ----------------------------------------------
    known = set(on_disk)
    bad_links: list[str] = []
    for src, t in [("SKILL.md", body)] + [(n, (REFS / n).read_text(encoding="utf-8")) for n in on_disk]:
        for m in re.finditer(r"`(?:references/)?([a-z0-9-]+\.md)`", t):
            target = m.group(1)
            if target not in known and target != "SKILL.md":
                bad_links.append(f"{src} -> {target}")
    check("all cross-references point at real files", not bad_links, "; ".join(sorted(set(bad_links))))

    # --- plugin marketplace manifests ------------------------------------------------
    mp_path = ROOT / ".claude-plugin" / "marketplace.json"
    if mp_path.is_file():
        import json
        try:
            mp = json.loads(mp_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            check("marketplace.json is valid JSON", False, str(exc))
            mp = None
        if mp:
            check("marketplace.json has name + owner.name + plugins",
                  bool(mp.get("name")) and bool(mp.get("owner", {}).get("name")) and bool(mp.get("plugins")))
            entry = (mp.get("plugins") or [{}])[0]
            check("plugin entry has name + source",
                  bool(entry.get("name")) and bool(entry.get("source")))
            src = ROOT / str(entry.get("source", "")).lstrip("./")
            check("plugin source directory exists", src.is_dir(), str(src))
            # A plugin's skills load from skills/<name>/SKILL.md under its source.
            plugin_skill = src / "skills" / entry.get("name", "") / "SKILL.md"
            check("plugin skill resolves at skills/<name>/SKILL.md",
                  plugin_skill.is_file(), str(plugin_skill))
            if plugin_skill.is_file():
                check("plugin skill copy matches the source SKILL.md",
                      plugin_skill.read_text(encoding="utf-8") == text,
                      "run: python scripts/build.py")
            pj_path = src / ".claude-plugin" / "plugin.json"
            check("plugin.json exists", pj_path.is_file(), str(pj_path))
            if pj_path.is_file():
                pj = json.loads(pj_path.read_text(encoding="utf-8"))
                check("plugin.json name matches the marketplace entry",
                      pj.get("name") == entry.get("name"),
                      f"{pj.get('name')!r} vs {entry.get('name')!r}")
                # Versions must agree, or users install something mislabelled.
                import re as _re
                m = _re.search(r"^##\s*\[(\d+\.\d+\.\d+)\]", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), _re.M)
                ver = m.group(1) if m else None
                check("marketplace, plugin.json and CHANGELOG versions agree",
                      ver is not None and entry.get("version") == ver and pj.get("version") == ver,
                      f"changelog={ver} marketplace={entry.get('version')} plugin={pj.get('version')}")

    print()
    if warnings:
        print(f"{len(warnings)} warning(s): {', '.join(warnings)}")
    if failures:
        print(f"FAILED: {len(failures)} check(s): {', '.join(failures)}")
        return 1
    print(f"Skill is valid: {len(lines)}-line SKILL.md, {len(on_disk)} references.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
