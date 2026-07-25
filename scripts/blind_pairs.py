#!/usr/bin/env python3
"""Build a blinded A/B comparison file for the skill-vs-baseline eval, plus the unblinding key.

The two previous graders knew they were grading *the skill*, which is fine for a single-arm
run and fatal for a comparison. This shuffles which arm appears as "Response A" per case,
writes the grader's file with no arm labels, and keeps the mapping in a separate key file
that the grader is never given.

The shuffle is seeded so the run is reproducible — the seed is passed in, not generated,
because scripts in this repo must not depend on wall-clock or unseeded randomness.

Usage:  python scripts/blind_pairs.py <seed>
Writes: evals/results/_blinded_pairs.md   (for the grader)
        evals/results/_unblinding_key.json (NOT for the grader)
"""
from __future__ import annotations

import glob
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "evals" / "results"


def load_arm(pattern: str) -> dict[str, str]:
    """Parse ===ANSWER <id>=== blocks out of every file matching the pattern."""
    answers: dict[str, str] = {}
    for f in sorted(RES.glob(pattern)):
        text = f.read_text(encoding="utf-8")
        parts = re.split(r"===ANSWER (.+?)===", text)
        # parts[0] is preamble; then alternating id, body
        for i in range(1, len(parts) - 1, 2):
            body = parts[i + 1].split("===END===")[0].strip()
            if body:
                answers[parts[i].strip()] = body
    return answers


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python scripts/blind_pairs.py <seed>")
        return 2
    seed = int(sys.argv[1])

    control = load_arm("_ctrl_*.md")
    treatment = load_arm("_treat_*.md")
    cases = [json.loads(l) for l in (ROOT / "evals" / "behavior.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]

    missing = [c["id"] for c in cases if c["id"] not in control or c["id"] not in treatment]
    if missing:
        print(f"ERROR: missing answers for: {missing}")
        return 1

    rng = random.Random(seed)
    key: dict[str, dict[str, str]] = {}
    out = [
        "# Blinded A/B comparison",
        "",
        "Two different AI assistants answered each question below. For every case you are given",
        "**Response A** and **Response B**. They are presented in a randomised order that varies",
        "case by case — A is not consistently the same assistant, and you are not told which is",
        "which. Grade each response independently against that case's criteria.",
        "",
        "---",
        "",
    ]

    for c in cases:
        cid = c["id"]
        flip = rng.random() < 0.5
        a_arm, b_arm = ("control", "treatment") if flip else ("treatment", "control")
        a_text = control[cid] if a_arm == "control" else treatment[cid]
        b_text = control[cid] if b_arm == "control" else treatment[cid]
        key[cid] = {"A": a_arm, "B": b_arm}

        out += [
            f"## CASE: {cid}",
            "",
            f"**Question asked:** {c['question']}",
            "",
            "### Response A",
            "",
            a_text,
            "",
            "### Response B",
            "",
            b_text,
            "",
            "---",
            "",
        ]

    (RES / "_blinded_pairs.md").write_bytes("\n".join(out).encode("utf-8"))
    (RES / "_unblinding_key.json").write_bytes(
        json.dumps({"seed": seed, "key": key}, indent=2).encode("utf-8")
    )

    flips = sum(1 for v in key.values() if v["A"] == "control")
    print(f"Blinded {len(cases)} cases (seed {seed}).")
    print(f"  control appears as A in {flips}/{len(cases)} cases — shuffle is working")
    print(f"  grader file: evals/results/_blinded_pairs.md")
    print(f"  key (withhold): evals/results/_unblinding_key.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
