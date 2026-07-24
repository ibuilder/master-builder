#!/usr/bin/env python3
"""Build every distributable artifact for the Master Builder skill from the single
source of truth (SKILL.md + references/). Run this after editing the skill; the
outputs are generated so they can never drift from the source.

Produces, in dist/:
  master-builder.skill       installable Claude skill (zip; root folder = master-builder/)
  master-builder.zip         identical package, .zip extension for the claude.ai uploader
  master-builder.bundle.md   one-file portable bundle for ANY AI assistant
                             (ChatGPT, Gemini, Perplexity, or any API/model)

Usage:  python scripts/build.py
Requires only the Python 3 standard library. No third-party dependencies.
"""
from __future__ import annotations
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
REPO_URL = "https://github.com/ibuilder/master-builder"

# Files packaged into the installable Claude skill (root folder = master-builder/).
PACKAGE_FILES = ["SKILL.md", "CHANGELOG.md"] + [
    f"references/{p.name}" for p in sorted((ROOT / "references").glob("*.md"))
]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def version() -> str:
    m = re.search(r"^##\s*\[(\d+\.\d+\.\d+)\]", read("CHANGELOG.md"), re.M)
    return m.group(1) if m else "0.0.0"


def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_text, body) for a Markdown file with YAML frontmatter."""
    if text.startswith("---"):
        end = text.index("\n---", 3)
        return text[3:end].strip(), text[end + 4:].lstrip("\n")
    return "", text


def folded_description(frontmatter: str) -> str:
    """Extract the folded `description: >-` scalar as a single spaced string."""
    lines = frontmatter.splitlines()
    out: list[str] = []
    grabbing = False
    for ln in lines:
        if ln.startswith("description:"):
            grabbing = True
            continue
        if grabbing:
            if ln and not ln[0].isspace():  # next top-level key ends the scalar
                break
            out.append(ln.strip())
    return " ".join(w for w in out if w).strip()


def ref_table(skill_body: str) -> list[tuple[str, str]]:
    """Parse the reference table in SKILL.md -> [(filename, description), ...] in order."""
    rows = []
    for m in re.finditer(r"\|\s*`references/([^`]+)`\s*\|\s*(.+?)\s*\|", skill_body):
        rows.append((m.group(1), m.group(2).strip()))
    return rows


def build_bundle(ver: str) -> str:
    skill_raw = read("SKILL.md")
    fm, skill_body = split_frontmatter(skill_raw)
    desc = folded_description(fm)
    pitch = desc.split(". ")[0].strip()
    if pitch and not pitch.endswith("."):
        pitch += "."

    refs = ref_table(skill_body)
    # Fall back to alphabetical if the table can't be parsed.
    if not refs:
        refs = [(p.name, "") for p in sorted((ROOT / "references").glob("*.md"))]

    out: list[str] = []
    out.append("# Master Builder — portable knowledge bundle")
    out.append("")
    out.append(f"> {pitch}")
    out.append("")
    out.append(
        "This single file is the **complete Master Builder skill** — its reasoning protocol and full "
        "reference library — concatenated into one document so it can be used in **any** AI assistant, "
        "not just Claude. It is generated from the source at "
        f"{REPO_URL} (MIT-licensed) — do not edit by hand; edit the source and rerun `scripts/build.py`."
    )
    out.append("")
    out.append(f"**Version {ver}** · Source of truth: {REPO_URL}")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## How to use this in an AI assistant")
    out.append("")
    out.append(
        "- **ChatGPT (Custom GPT or Project)** — put the *Master Builder Protocol* section below into the "
        "Instructions / custom instructions, and upload the reference sections (or this whole file) as Knowledge.\n"
        "- **Google Gemini (Gem)** — paste this file into the Gem instructions, or attach it as a knowledge file.\n"
        "- **Perplexity (Space)** — create a Space, paste the protocol into the custom instructions, and add "
        f"this file (or the {REPO_URL} repo link) as a source.\n"
        "- **Any API / open model** — prepend this file to your system prompt.\n\n"
        "The one behavior you lose versus the native Claude skill is *progressive disclosure* — Claude loads "
        "only the reference a task needs, on demand. Here everything is loaded at once: simpler and universal, "
        "but heavier on context. For automatic triggering and load-on-demand, install the Claude skill itself "
        f"(see {REPO_URL})."
    )
    out.append("")
    out.append("---")
    out.append("")
    out.append("## What's inside")
    out.append("")
    out.append("1. **The Master Builder Protocol** — the core reasoning method (from `SKILL.md`).")
    for i, (name, d) in enumerate(refs, start=2):
        label = d if d else name
        out.append(f"{i}. **{name}** — {label}")
    out.append("")
    out.append("=" * 100)
    out.append("")
    out.append("# Part 1 — The Master Builder Protocol")
    out.append("")
    out.append("*(This is the skill's core instruction file. In Claude it is `SKILL.md`; its frontmatter, "
               "which only controls Claude's automatic triggering, has been removed here.)*")
    out.append("")
    out.append(skill_body.strip())
    out.append("")
    out.append("=" * 100)
    out.append("")
    out.append("# Part 2 — Reference library")
    out.append("")
    out.append("*(Each section below is one reference file. Consult the one that fits the task.)*")
    out.append("")
    for name, _ in refs:
        content = read(f"references/{name}").strip()
        out.append("-" * 100)
        out.append("")
        out.append(f"<!-- reference: {name} -->")
        out.append("")
        out.append(content)
        out.append("")
    out.append("=" * 100)
    out.append("")
    out.append(f"*Master Builder v{ver} — {REPO_URL} — MIT. Built with Claude.*")
    out.append("")
    return "\n".join(out)


# Reproducible builds: zip entries must not carry the wall-clock time, or two builds of
# identical source produce different bytes and CI's "dist is in sync" check fails forever.
# 1980-01-01 is the earliest timestamp the zip format can represent.
ZIP_EPOCH = (1980, 1, 1, 0, 0, 0)


def build_package(dest: Path) -> None:
    """Write the installable Claude skill zip.

    Arcnames use forward slashes on every OS, and entries carry a fixed timestamp so the
    output is byte-identical for identical input.
    """
    dest.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in PACKAGE_FILES:
            info = zipfile.ZipInfo(f"master-builder/{rel}", date_time=ZIP_EPOCH)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16  # stable, sane file mode
            # ZipInfo defaults create_system to 0 on Windows and 3 elsewhere, which makes
            # the same content produce different bytes per OS. Pin it so a build on Windows
            # matches a build on Linux (read_text already normalizes CRLF -> LF).
            info.create_system = 3
            z.writestr(info, read(rel))


def main() -> int:
    ver = version()
    DIST.mkdir(parents=True, exist_ok=True)

    build_package(DIST / "master-builder.skill")
    build_package(DIST / "master-builder.zip")

    bundle = build_bundle(ver)
    (DIST / "master-builder.bundle.md").write_text(bundle, encoding="utf-8", newline="\n")

    print(f"Built Master Builder v{ver}:")
    for f in ("master-builder.skill", "master-builder.zip", "master-builder.bundle.md"):
        p = DIST / f
        print(f"  dist/{f:<26} {p.stat().st_size:>7} bytes")
    print(f"  package files: {len(PACKAGE_FILES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
