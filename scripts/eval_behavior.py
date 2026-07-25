#!/usr/bin/env python3
"""Behavioural evaluation — does the skill obey its own stated conventions?

`eval_retrieval.py` proves the right reference is reachable. It cannot prove the *answer*
is any good. This file holds the other half: realistic questions paired with the
behaviours the skill promises (`SKILL.md` output conventions and professional boundaries,
and the specific rules in the references it routes to).

**These cannot be graded automatically here.** Grading an answer requires running a model
with the skill loaded and judging the output — so this script does not pretend to score
anything. It validates the eval set and prints a grading sheet. Reporting a green tick for
a check that never ran would be exactly the false assurance
`document-intelligence.md` §5 warns about.

How to actually run it:
  1. Load the skill (install it, or paste `dist/master-builder.bundle.md`).
  2. Ask each question below in a clean session.
  3. Grade the answer against its `must` / `must_not` criteria.
  4. A `must_not` hit is a hard failure — it means the skill asserted something it
     promises never to assert (a fabricated hazard value, an unstamped structural verdict,
     a carbon number with no boundary).

Usage:
  python scripts/eval_behavior.py            # validate the set + print the grading sheet
  python scripts/eval_behavior.py --check    # validate structure only (CI uses this)
  python scripts/eval_behavior.py --ids      # list case ids
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CASES = ROOT / "evals" / "behavior.jsonl"
REQUIRED_FIELDS = ("id", "question", "must", "must_not", "tests")


def load() -> list[dict]:
    cases = []
    for n, line in enumerate(CASES.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("//"):
            continue
        try:
            cases.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{CASES.name}:{n}: invalid JSON — {exc}")
    return cases


def check(cases: list[dict]) -> int:
    """Structural validation — CI runs this so the set can't rot into nonsense."""
    problems: list[str] = []
    seen: set[str] = set()
    for c in cases:
        cid = c.get("id", "<no id>")
        for f in REQUIRED_FIELDS:
            if f not in c:
                problems.append(f"{cid}: missing field '{f}'")
        if cid in seen:
            problems.append(f"{cid}: duplicate id")
        seen.add(cid)
        if not isinstance(c.get("must"), list) or not c.get("must"):
            problems.append(f"{cid}: 'must' must be a non-empty list")
        if not isinstance(c.get("must_not"), list) or not c.get("must_not"):
            problems.append(f"{cid}: 'must_not' must be a non-empty list")
        if len(str(c.get("question", ""))) < 15:
            problems.append(f"{cid}: question is too short to be realistic")

    for p in problems:
        print(f"  FAIL {p}")
    if problems:
        print(f"\nFAILED: {len(problems)} problem(s) in {CASES.name}")
        return 1
    print(f"  ok   {len(cases)} behaviour cases, all well-formed")
    return 0


def sheet(cases: list[dict]) -> None:
    print("=" * 78)
    print("MASTER BUILDER — BEHAVIOURAL GRADING SHEET")
    print("=" * 78)
    print("Ask each question with the skill loaded, then grade the answer.")
    print("A must_not hit is a HARD FAILURE — the skill broke a promise it makes.\n")
    for i, c in enumerate(cases, 1):
        print(f"[{i:>2}] {c['id']}")
        print(f"     Q: {c['question']}")
        for m in c["must"]:
            print(f"     [ ] MUST      {m}")
        for m in c["must_not"]:
            print(f"     [ ] MUST NOT  {m}")
        print(f"     tests: {c['tests']}\n")
    print("=" * 78)
    print(f"{len(cases)} cases. Score = cases with every MUST met and no MUST NOT hit.")
    print("Record the result and the date; an ungraded set proves nothing.")


def main() -> int:
    cases = load()
    if "--ids" in sys.argv:
        for c in cases:
            print(c["id"])
        return 0
    rc = check(cases)
    if rc or "--check" in sys.argv:
        return rc
    print()
    sheet(cases)
    return 0


if __name__ == "__main__":
    sys.exit(main())
