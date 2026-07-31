# Cross-model run — does the skill transfer to a weaker model?

- **Date:** 2026-07-31 · **Skill version:** 0.16.0 · **Model:** Claude Haiku 4.5 (both arms)
- **Cases:** 8 diagnostic subset of `evals/behavior.jsonl` — the three the Opus control previously
  failed, the three it tied on, and two it partially passed.

## Why a weaker model, and what this is *not*

The standing limitation after the 2026-07-25 baseline was **single model family**. That limitation is
**not fully lifted here**: a true cross-*vendor* test (GPT, Gemini) is not runnable from this
environment, and remains undone.

What this *does* test is arguably the sharper question. The baseline could not separate
**"the skill supplies knowledge"** from **"the model already knew, and the skill supplied style."** A
smaller model has less latent domain knowledge to fall back on — so if the skill carries genuine
content, the lift should be **larger**, not smaller.

Same design as the baseline: identical prompts but for one line, responses paired A/B with **arm order
randomised per case** (seed 20260731; control appeared as A in 4/8), graded by an agent told only that
two assistants answered and barred from the key.

## Result

| | PASS | PARTIAL | FAIL |
|---|---|---|---|
| **Haiku, no skill** | **1 / 8** | 5 | 2 |
| **Haiku + skill** | **6 / 8** | 1 | 1 |

Five of eight cases changed verdict, all in the skill's favour; none went the other way.

| case | no skill | + skill |
|---|---|---|
| `hazard-value-honesty` | PARTIAL | **PASS** |
| `cost-conventions` | PARTIAL | **PASS** |
| `universal-vs-local` | PARTIAL | **PASS** |
| `code-threshold-recall` | **FAIL** | **PASS** |
| `pushback-hazard` | PARTIAL | **PASS** |
| `no-location-given` | PASS | PASS *(tie)* |
| `structural-boundary` | PARTIAL | PARTIAL *(tie)* |
| `numeric-sanity` | **FAIL** | **FAIL** *(tie — see below)* |

**The lift is larger on the weaker model.** Opus went 50% → 94% (9/18 → 17/18); Haiku goes
**12.5% → 75%** (1/8 → 6/8). That is the direction predicted if the skill is supplying knowledge
rather than polish, and it is the strongest evidence yet against the "it was just the model" reading.

## Where the skill failed, and it matters more than the wins

**`numeric-sanity` failed in BOTH arms.** Both quoted indoor leafy-greens energy **6–20× above** the
published ~10–40 kWh/kg fresh-weight range. v0.11.0 added a "sanity-check the band a second way" rule
*specifically* because of this defect, and added a regression case to guard it. **On a weaker model the
rule did not hold.**

Worse, and the single most useful finding in this run: one answer **performed** the sanity check and
the check was **itself wrong by a factor of 1,000** — computing GWh where its own rate gave MWh, with a
dollar figure that silently agreed with the wrong reading. The verification step verified nothing while
looking exactly like diligence.

That is **ritual compliance**: the skill successfully induced the *form* of the check on a model that
could not execute it. A rule that produces the appearance of verification without the substance is a
net negative, because it launders the original error.

**Also failed to transfer:** `structural-boundary` stayed PARTIAL in both arms — neither named AHJ
approval, though the Opus skill arm did. And cost magnitudes were badly off in both arms (one band low
by 4–6×), again with no order-of-magnitude check.

## A defect in the skill itself

The grader caught an **internal reference filename leaking into user-facing prose** (`global-codes.md
§2`). The references cross-link each other by filename for navigation; a model can surface that to a
user as though it were a citation. Fixed in v0.17.0 — filenames are navigation, never citations, and
the user gets the actual code section or standard instead.

## What changed as a result

1. **"A check you cannot verify is not a check."** Added to SKILL.md output conventions: carry the units
   through the check and confirm it lands in the same order of magnitude as the claim.
2. **Reference filenames are navigation, not citations.** Added to SKILL.md.
3. Recorded here that **the sanity-check rule is capability-dependent** — it works on a stronger model
   and degrades to ritual on a weaker one. That is a real bound on what this skill can promise.

## Limitations

- **Still single-vendor.** Cross-provider transfer remains untested and unclaimed.
- **n=1 per case per arm**, 8 cases — directional, not a stable rate.
- The bundle was handed over directly, so trigger and retrieval reliability are not exercised.
- The grader is the same model family as both arms.
