# Construction Document Intelligence

Most of a project's truth is trapped in documents — a 500-page spec book, an 89-sheet drawing set, a
change-order proposal, a pay application. Read this when the task is to **extract reliable numbers from
construction documents**, cross-check documents against each other, judge whether **AI-generated**
design output can be trusted, or build tooling that does any of it.

The governing idea: **a number's trustworthiness is a property of how it was derived, not of how
confident it sounds.** A count read from a door schedule and a length scaled off pixels are not the same
kind of fact, and presenting them with equal certainty is the defect. Everything below follows from that.

## Contents
1. Index once, query many
2. Confidence by provenance — the reliability rule
3. Sanity checks: encode what is physically possible
4. Never trust a column that survived text-linearisation
5. Coverage-aware findings — "0 findings" is not a clean bill of health
6. Cross-document coordination — where change orders are born
7. Generated output: plausible is not buildable
8. Units, grades, and canonical identity
9. Writing back to documents — never in place
10. Deterministic finding vs. judgment call
11. Applying it

---

## 1. Index once, query many

Contractors receive **flattened PDFs, not the model** — the structured data that existed in BIM is
discarded on export. But a native construction PDF still carries a **vector text layer** holding the real
sheet numbers, tags, schedules, and printed dimensions. That layer is the cheap, accurate path in.

There are three ways to answer a question about a drawing set, and they are not close:

| Approach | Cost | Reliability |
|---|---|---|
| Feed raw drawing **images** into the prompt | Highest | Lowest — the model infers from pixels and mis-weights detail buried in a huge context |
| Read the **vector text** each time | Moderate | Good |
| **Build an index once, then query it** | Lowest | Highest — deterministic and repeatable |

So: **parse the set once into a structured store (a small database), then answer every subsequent
question from that store.** Reported token savings on real sets run to one or two orders of magnitude,
but the reliability gain matters more — the same question asked twice returns the same answer, and every
answer can cite the sheet it came from.

This is `build-doctrine.md` §2 ("do heavy work at the right layer; stream light artifacts") applied to
documents, and §1 (stable identity) applied to sheets and marks.

> **Build a map before you build the index's consumers.** A one-page **sheet index** — every sheet, its
> discipline, its scale, and what is on it — lets you query straight to the sheet that holds the answer
> instead of scanning everything. It is progressive disclosure for a drawing set: read the map first,
> then open only what the task needs.

Two-pass extraction is usually the right shape: a **fast pass** over every sheet for tags, scales, and
printed dimensions, then a **slow, targeted pass** (table/schedule detection is expensive) aimed only at
the sheets that actually carry schedules. Cache the result; a rebuilt index should be a no-op.

> **Use the right technique for the right job — this is not "text always beats vision."** Pattern
> matching over the text layer is the correct tool for **extracting known, structured things** (a tag
> format, `F'c = X MPa`, a schedule row). It is the *wrong* tool for **classifying a sheet**, because
> title blocks, naming, and layout vary wildly between offices and no regex survives that variation. For
> "what kind of drawing is this and what's on it," read the rendered sheet with vision. Rule of thumb:
> **vision to classify and orient; text to extract and count; the database to answer.**

---

## 2. Confidence by provenance — the reliability rule

Tag every extracted number with **how it was obtained**, and carry that tag all the way to the user. A
workable ladder for drawings:

| What you want | How it's derived | Confidence |
|---|---|---|
| Count of an element type | Read from a **schedule table** (door/window/column schedule) | **High** |
| Count of an element type | Counted from **tag callouts** on sheets | **Medium** — tags get missed, duplicated across sheets, or repeated in details |
| A dimension | The designer **printed it** on the sheet (`205'-6"`) | **High** |
| A distance | **Scaled from pixels** via the scale bar | **Low** — never quote without a sanity check |
| A value from prose | Regex/LLM extraction from paragraph text | **Medium** — verify against the source page |

Two rules follow:
- **State the confidence whenever you hand over the number.** "147 doors (high — from the door schedule
  on A-601)" is a usable fact; "147 doors" is a liability.
- **Flag the derivation path when it is weak.** A number that came from reading a *scanned image* rather
  than vector text must be marked as such and verified against the source page by a human. A
  picture-read number must never be presented with the same certainty as vector text.

This is the estimate-class discipline (`construction-delivery.md` §3) and honest-status doctrine
(`build-doctrine.md` §7) applied to extraction: **a ROM is not a GMP, and a scaled pixel is not a
printed dimension.**

---

## 3. Sanity checks: encode what is physically possible

Extraction fails loudly if you let it. Encode domain bounds so nonsense is caught at extraction time
rather than in a bid:

- A measured run **longer than the building footprint** is wrong.
- A door count exceeding the room count by an order of magnitude is wrong.
- A concrete strength of 2.5 psi or 250,000 psi is a unit error, not a mix design.
- A single line item that is a large fraction of the whole contract deserves a second look
  (`pro-forma-review.md` §5).

Store the check result alongside the value (`passed` / `flagged`) and make the flagged set queryable —
"show me everything that failed sanity" is the highest-yield review a human can run. This is
**compliance-as-code** (`build-doctrine.md` §8): make the invalid state visible at creation.

---

## 4. Never trust a column that survived text-linearisation

A specific, expensive trap worth naming precisely.

When a PDF is linearised to text, **column alignment is not preserved reliably**. In a priced
change-order or schedule-of-values table, the extended amount printed in the right-hand column often
lands on a *different text line* than the description it belongs to. Tie out against those extracted
extensions and you will manufacture discrepancies on a document whose arithmetic is perfectly correct —
and you will burn your credibility with the person you handed the report to.

**The rule: read the atomic inputs, then recompute.** Take *quantity* and *rate* from the line, compute
`quantity × rate` yourself, and compare that to the total. Never treat a linearised `$` column as
authoritative. If you catch yourself thinking "let me just check the printed total," stop — that is the
failure mode.

Generalized: **prefer values you can recompute from primitives over values you merely read**, wherever
layout may have been destroyed in extraction.

---

## 5. Coverage-aware findings — "0 findings" is not a clean bill of health

The most important rule in this file, and the one most often missing from audit tooling.

An audit that reports "no issues found" without saying **which checks actually ran** is worse than no
audit, because it manufactures false assurance. A change order checked without the contract's rate
schedule can return zero findings while being riddled with unit-price inflation — the check simply could
not see it. An image-only PDF yields zero extracted sheets; that is a **sourcing gap, not a clean set**.

**Always report coverage alongside findings:**

```
0 findings — but only 2 of 4 checks had the data to run
  [checked]     markup / O&P caps
  [checked]     labor rates            (rate schedule supplied)
  [NOT CHECKED] unit prices            — no contract rate schedule provided
  [NOT CHECKED] quantities vs drawing  — no drawing set provided
```

Say the same thing in prose when you report to a human: *what was verified, what was not, and why.*
Absence of evidence is not evidence of absence, and a reviewer who learns that the hard way stops
trusting the tool — correctly. This is the document-review expression of `pro-forma-review.md`'s
reconciliation discipline and the honest-status rule.

---

## 6. Cross-document coordination — where change orders are born

A project is described by several documents that are **written by different people at different times
and almost never fully agree.** The spec book says minimum f′c = 30 MPa; the structural drawings show
25/30/35 MPa mixes by element; the drawings cite ASTM A307 for anchor bolts and the spec never mentions
it. Each of those gaps is a coordination item that, undetected, becomes an RFI at best and a change order
at worst.

Comparing a 500-page spec against a 50-sheet set by eye is hours of an estimator's time and is
unreliable. Indexing both and **joining them fact-by-fact** takes seconds and cites the page on each
side. High-value fact families to compare:

- **Material strengths** — concrete f′c, masonry f′m, steel grades.
- **Reinforcement** — spec and grade (ASTM A615 Grade 60; CSA G30.18 Grade 400W).
- **Referenced standards coverage** — a standard cited on the drawings but absent from the spec (or vice
  versa) is a real gap.
- **Schedules vs. plans** — quantities and marks that disagree between the schedule and the sheet.
- **Finishes, assemblies, and rated construction** — where the fire rating on the drawing meets the
  assembly in the spec.

**Report each result in one of five states, and cite both pages:** `MATCH`, `MISMATCH`, `VERIFY`,
`SPEC-ONLY`, `DRAWING-ONLY`.

> **A flagged join is a coordination item to confirm, not a defect to allege.** The tool finds where two
> documents disagree; a human decides which one governs — the contract documents have an order of
> precedence, and it is often the spec. Overclaiming here is how a useful report becomes an argument.

This is the same instinct as the **decision-readiness / RFI-prevention audit** in `digital-toolkit.md`:
resolve the conflict before it costs money, and do it on paper rather than in the field.

> **A join finds contradictions. It will never find an omission.** Everything above compares what *is*
> in two documents. The more dangerous defect is a requirement that appears in **neither** — the
> standard nobody cited, the accessibility clause nobody applied, the testing regime nobody scheduled.
> No amount of cross-referencing surfaces it, because there is nothing to cross-reference.
>
> Catching it needs a deliberately different, **three-pass** shape:
> 1. **What the documents already address** — extract every code citation, standard, and requirement
>    actually present in the specs, drawings and schedules.
> 2. **What *should* apply** — research what governs this scope, in this jurisdiction, for this
>    occupancy, *independently of what the documents say.*
> 3. **The delta** — report only what is in (2) and missing from (1), each with a confidence level and a
>    citation on both sides.
>
> Pass 2 is the one that cannot be skipped or derived from the project file, and it is the whole value:
> you are testing the documents against the world, not against themselves. Report the result as
> **gaps to confirm, not defects to allege** — and apply §5, because a gap analysis run without the
> jurisdiction resolved has not checked anything.

---

## 7. Generated output: plausible is not buildable

Everything above is about reading documents. The mirror problem is **AI that produces** them — a
layout, a detail, a framing plan, a fit-out. Here the failure mode inverts: instead of a number that
looks precise and is wrong, you get **geometry that looks right and cannot be built.**

The evidence is unambiguous. The **DreamHouse** benchmark ([arXiv 2603.24866](https://arxiv.org/abs/2603.24866),
2026) tests exactly this — over 26,000 timber-frame structures across 13 architectural styles, verified
to **LOD 350**, scored by a deterministic 10-test structural validation framework. Its finding:

> **"Physical validity is not a byproduct of visual imitation, and vice versa."**

Concretely, the best model reached a **joint** structural-and-visual pass rate of just **7.1%**, and the
two axes came apart entirely between models — one led structurally (79.2%) while scoring *lowest*
visually; another led visually and not structurally. Note the distinction, because it is easy to
misquote: **structural pass rates alone are far higher than 7.1%**; it is passing *both* that collapses.
The paper also warns that **"physical constraints are discontinuous"** — a near-miss in topology is not
a near-miss in buildability. Something can be one member away from standing up and still fall down.

**What follows for practice:**

- **Never accept a render, plan, or model as evidence of feasibility.** Visual review is a check on
  *intent*, not on *constructability*. They are separate reviews with separate reviewers.
- **Validate generated geometry against a deterministic engine**, not another model — clash, span and
  load checks, code pre-checks, dimensional and clearance rules. The neuro-symbolic pattern (a learned
  generator inside hard, rule-based constraints) exists precisely because the generator cannot police
  itself. This is `build-doctrine.md` §8's compliance-as-code, pointed at generated output.
- **Constrain generation up front rather than reviewing after.** Encode the codes, the firm's standards,
  and the geometric rules as bounds on what can be produced. Cheaper than catching it downstream, and
  it makes the invalid state unrepresentable.
- **The stamp does not move.** A generated structural scheme is a starting point for an engineer of
  record, never a substitute (see SKILL.md professional boundaries).

> **How you frame the task beats which model you use.** The same benchmark found that
> **"protocol dominates model"** — one model swung from a **45.4% to 78.5%** structural pass rate,
> **33 points**, purely by changing the task scaffolding, a gap larger than the differences between
> models under a fixed protocol. This is the generation-side statement of §1: **externalise the problem
> into a structured, queryable form and constrain the step before you ask for the answer.** If output
> quality disappoints, restructure the task before reaching for a different model.

## 8. Units, grades, and canonical identity

Cross-document comparison fails on naming long before it fails on logic:

- **Normalize units before comparing**, and keep one canonical internal unit (e.g. everything to psi;
  MPa → psi ×145.038). Cross-unit projects are common and dangerous — metric drawings bid against an
  imperial spec, or a metric spec with imperial rebar callouts.
- **Canonicalize designations** so the same thing matches itself: `ACI 318-14` must match `ACI 318`;
  `ASTM A615/A615M` must match `ASTM A615`. Edition suffixes and dual-designation slashes are the two
  usual culprits.
- **Equivalent grades across regimes** are not string-equal: ASTM A615 Grade 60 vs CSA G30.18 Grade 400W
  describe comparable reinforcement in different systems. Map deliberately; never assume.
- Keep the **stable identity** of a sheet or a mark (sheet number + revision, door mark) as the key
  everything else hangs from — `build-doctrine.md` §1. Identity drift is the root of most false mismatches.

---

## 9. Writing back to documents — never in place

Extraction is read-only and safe. **Modifying** documents — bulk stamps, revision clouds, markup edits
across a set — is not, and it earns the irreversible-action rails from `build-doctrine.md` §6:

- **Never modify the source file.** Write to a new output; the original stays pristine and re-runnable.
- **Emit a register of what changed** — every stamp, edit, and clouded region, as a list a human can
  audit. A bulk operation without a record of what it touched is unreviewable.
- **Confirm the operation before running it at scale.** State the source, the target sheets, and the
  exact operation, and get a human yes. A mis-scoped bulk markup across an 89-sheet set is expensive to
  unpick.
- Remember what a markup *is*: on an issued drawing it is a **contractual communication**. "Not for
  Construction" applied to the wrong sheets, or removed from the right ones, has consequences beyond the
  PDF.

## 10. Deterministic finding vs. judgment call

Separate the two and never blur them:

- **Deterministic finding** — a fact that arithmetic or a document join settles. "The markup applied is
  22%; the contract caps it at 15% — the overcharge is $1,320.32, page 4." This can be asserted.
- **Judgment call** — "is 42 hours reasonable for this scope?" This must be *surfaced for a human*, with
  the evidence, and not ruled on.

For an owner-side reviewer, a wrong accusation is far more costly than a missed catch: it damages the
relationship and the reviewer's credibility in one move. **Bias toward silence on judgment and precision
on arithmetic.** This mirrors the split in `pro-forma-review.md` §7 between model-integrity issues
(arithmetic that must be fixed) and judgment issues (assumptions that must be defended) — they are
addressed differently and must be reported differently.

---

## 11. Applying it

When building or evaluating any construction-document tooling — or doing the review by hand — run these:

- Is there an **index built once** and queried many times, rather than re-reading source documents?
- Is there a **map** (sheet index / spec index) read before the detail?
- Does every number carry its **provenance and confidence**, all the way to the user?
- Are there **sanity bounds** encoded, and can you list what failed them?
- Are values **recomputed from primitives** rather than trusted from a possibly-mangled layout?
- Does the output report **coverage** — which checks ran and which could not, and why?
- Are cross-document results **page-anchored on both sides** and stated as items to confirm?
- Are **units and designations canonicalized** before anything is compared?
- Are **deterministic findings and judgment calls** clearly separated?
- Is the human kept as the decider on anything contractual, and is the tool's output **auditable**?

> **Attribution.** The practical lessons in §§1–8 — index-once/query-many, confidence-by-provenance,
> the text-linearisation trap, and coverage-aware reporting — were sharpened by studying the open
> `autoConst` construction-document skills by Hamza Abdul Jabbar
> (github.com/hamzaabduljabbar), which implement these ideas as working tools. The doctrine here is
> written independently for this skill; the tools themselves are separate projects with their own terms.
