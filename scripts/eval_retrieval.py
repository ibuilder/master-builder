#!/usr/bin/env python3
"""Retrieval evaluation — does the corpus actually answer the questions people ask,
and does the material live in the reference you'd reach for?

`validate.py` proves the skill is well-formed and the MCP self-test proves the server
speaks the protocol. Neither proves the *content* is any good. This closes that gap for
the part that can be checked deterministically: for each realistic question in
`evals/retrieval.jsonl`, score every reference by how strongly it matches the question's
salient terms, and assert the reference a builder would expect ranks first.

It catches two real regressions:
  * **Coverage loss** — a topic quietly stops being covered (score collapses).
  * **Placement drift** — content migrates to the wrong file, so on-demand loading
    (progressive disclosure) pulls the wrong reference and the answer degrades.

This is the `build-doctrine.md` §5 staged-validation gate applied to the skill itself.
It does NOT evaluate answer quality — that needs a model; see `evals/behavior.jsonl`.

Usage:  python scripts/eval_retrieval.py [-v]
Exit 0 = every case routed correctly. Stdlib only.
"""
from __future__ import annotations

import json
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "references"
CASES = ROOT / "evals" / "retrieval.jsonl"


def fold(s: str) -> str:
    """Lowercase + strip accents, matching the MCP server's search behaviour."""
    return "".join(
        c for c in unicodedata.normalize("NFD", s.lower())
        if unicodedata.category(c) != "Mn"
    )


def load_corpus() -> dict[str, str]:
    return {p.name: fold(p.read_text(encoding="utf-8")) for p in sorted(REFS.glob("*.md"))}


def load_cases() -> list[dict]:
    cases = []
    for line in CASES.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("//"):
            cases.append(json.loads(line))
    return cases


def score(corpus: dict[str, str], terms: list[str]) -> list[tuple[str, int]]:
    """Rank references by total occurrences of the question's salient terms."""
    scored = [(name, sum(text.count(fold(t)) for t in terms)) for name, text in corpus.items()]
    # Sort by score desc, then name for stable ties.
    return sorted(scored, key=lambda kv: (-kv[1], kv[0]))


def main() -> int:
    verbose = "-v" in sys.argv or "--verbose" in sys.argv
    corpus = load_corpus()
    cases = load_cases()
    failures: list[str] = []

    print(f"Retrieval eval — {len(cases)} cases over {len(corpus)} references\n")

    for case in cases:
        ranked = score(corpus, case["terms"])
        top, top_score = ranked[0]
        expected = case["expect"]  # any one of these ranking first is a pass
        ok = top in expected and top_score > 0

        if ok:
            print(f"  ok   {case['id']:<22} -> {top} ({top_score})")
        else:
            print(f"  FAIL {case['id']:<22} -> got {top} ({top_score}), expected one of {expected}")
            print(f"       q: {case['question']}")
            failures.append(case["id"])

        if verbose or not ok:
            for name, sc in ranked[:4]:
                mark = "*" if name in expected else " "
                print(f"         {mark} {sc:>4}  {name}")

    print()
    total = len(cases)
    passed = total - len(failures)
    print(f"{passed}/{total} routed to the expected reference "
          f"({100 * passed // total if total else 0}%)")
    if failures:
        print(f"FAILED: {', '.join(failures)}")
        print("\nA failure means the topic is missing, thin, or living in the wrong file — "
              "fix the content or, if the expectation was wrong, fix the case.")
        return 1
    print("Every question routes to the reference a builder would reach for.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
