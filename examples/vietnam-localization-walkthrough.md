# Worked example — localizing for a jurisdiction the skill has never seen

**What this demonstrates:** the six-resolution **localization procedure**
(`references/jurisdiction-dossiers.md` §1) applied to a country with **no dossier in this skill** and
**no entry in its code-family router**. The Hempstead case study shows the skill auditing a model; this
one shows it landing somewhere unfamiliar without bluffing.

**The brief:** a mid-rise commercial building in **Ho Chi Minh City, Vietnam**. Foreign developer, no
local team yet, asking the question every developer asks first — *what governs, who approves, and how
long does it take?*

**Read this for the shape of the output, not the values.** Everything below is dated 31 July 2026 and
carries its own verification status. That is the point of the exercise: a localization that hands you
confident-sounding specifics is doing the dangerous thing.

---

## R1 — Resolve the place, to the right depth

Country → province/municipality → district → **plot**. Vietnam runs a **People's Committee** structure,
and construction-permit authority is **decentralised** to that hierarchy — so "Vietnam" is not the unit
of analysis, and neither is "Ho Chi Minh City" on its own.

The 2020 amendment to the Law on Construction moved permitting for **special-grade works** from the
Ministry of Construction **down** to the local People's Committee. Which committee, at which level,
depends on the project's assigned **grade** — so the first real question is not *where* but **what
grade is this work**, because grade drives who approves it.

> **To verify:** the current grade classification for this building type and scale, and which People's
> Committee level that lands on. → ask a locally licensed consultant, not a search engine.

## R2 — Resolve the code stack, and the edition actually adopted

Vietnam's technical system rests on two pillars, and conflating them is the classic outsider error:

- **QCVN — National Technical Regulations.** **Mandatory.** Issued by competent state agencies in the
  form of a *Circular*. This is the legally binding layer. Example: **QCVN 06:2022/BXD**, fire safety of
  buildings.
- **TCVN — National Standards.** The standards layer beneath, referenced by and supporting the QCVN.

Above both sits the **Law on Construction** and its implementing decrees (e.g. **Decree
15/2021/ND-CP**, which governs the permit application process).

**And here is the reason this example exists.** An **amended Law on Construction was passed on
10 December 2025 and took effect on 1 July 2026** — roughly four weeks before this walkthrough was
written. Any guidance, briefing note, or model recollection predating mid-2026 may describe a
superseded regime.

> This is R2's whole purpose: **the published edition is not the enforced edition, and "current" has a
> date.** A confident answer assembled from 2024 sources would be describing a law that has since been
> replaced. Confirm which text governs an application lodged *today*, and whether transitional
> provisions apply to projects already in train.

## R3 — Resolve the AHJ set — everyone who can say no

The building permit is one gate. Enumerate the rest before programming anything:

- **People's Committee** at the applicable level — the construction permit itself.
- **Design appraisal** — Vietnam has an appraisal step for construction design after basic design;
  notably, the 2020 amendment created a **permit exemption** for works whose post-basic design has been
  appraised. That is a genuine programme lever *if* it applies, and a trap if assumed.
- **Fire prevention and fighting authority** — a separate approval track under the fire regulation
  (QCVN 06 family). As in the Gulf (`jurisdiction-dossiers.md` §4), treat fire as a first-class parallel
  authority, not a closeout item.
- **Environmental** approval, **land-use rights** (critical and distinctive — see R5), utilities, and
  aviation/heritage overlays where applicable.

> **To verify:** whether the appraisal-based permit exemption reaches this project type, and the actual
> fire-approval sequence and duration in this district.

## R4 — Resolve the climate and hazard basis

Physics, and the half of the brief that does not change with the law
(`references/climate-building-science.md`):

Ho Chi Minh City is **Köppen Aw** — tropical savanna: hot year-round, very high humidity, a pronounced
monsoon. That fixes several things immediately and *without needing a code lookup*:

- **Cooling-dominated.** The air-conditioned interior is the cool, dry side, so the vapour drive is
  **inward**. Vapour control belongs toward the **exterior**; interior finishes must stay **permeable**
  so the assembly dries inward. An impermeable interior finish here is a mould factory.
- **Rain and drainage govern the envelope** — deep overhangs, rain screens, and stormwater sized to
  monsoon intensity, not to a temperate design storm.
- **Flood and subsidence are live**, and low-lying delta ground raises foundation, dewatering and
  long-term settlement questions.
- Corrosion and biological attack (mould, termites) drive durability and material selection.

> **To verify from local maps and the QCVN, never from memory:** design wind (typhoon exposure varies
> markedly along the coast), rainfall intensity, flood datum, soil profile and groundwater.

## R5 — Resolve the market and delivery conventions

- **Land tenure is the distinctive one.** Vietnam's regime is built on **land-use rights** rather than
  freehold ownership as an outsider would understand it, with different rules for foreign-invested
  entities. This is not a detail — it sits underneath the entire capital structure and the exit, and it
  is the item most likely to invalidate a pro forma built on Anglo-American assumptions.
- Currency (VND), escalation, import exposure on equipment and finishes, and contractor capability tiers.
- **FIDIC** is common on internationally financed work; domestic contracts follow local forms.

> **To verify:** the current foreign-ownership and land-use-right position for this entity type and
> asset class — a question for Vietnamese counsel, before the model, not after.

## R6 — Resolve who may design, stamp, and build

Expect **mandatory local licensure** for the design and appraisal roles, and a registered local
contractor. A foreign practice normally pairs with a local architect and engineer of record who carry
the submission. Confirm the practising-certificate requirements for each role.

---

## What the localization actually produced

**Resolved with reasonable confidence** — the *structure*: two-pillar QCVN/TCVN system with QCVN as the
mandatory layer; decentralised People's Committee permitting driven by works grade; a design-appraisal
step that can exempt the permit; fire as a separate parallel authority; land-use rights rather than
freehold; mandatory local licensure. **And the climate consequences, which are physics and need no
permission slip**: vapour control outward-facing, permeable interior finishes, monsoon-sized drainage,
delta-ground foundations.

**Explicitly not resolved** — the works-grade classification and therefore the approving committee;
whether the appraisal exemption reaches this project; realistic durations for each gate; every hazard
value; the foreign-ownership position; and **which version of the Law on Construction governs an
application lodged today**, given the 1 July 2026 change.

**The critical path is the answer.** Not the code list — the *sequence*: land-use rights → investment
approval → design appraisal → permit (or exemption) → fire approval, with the fire track running
parallel throughout. Approval duration is a financing cost (`references/real-estate-finance.md` §5),
and on a jurisdiction this unfamiliar the honest first deliverable is **a list of what to confirm and
who can confirm it**, priced as weeks, not a schedule pretending to certainty.

---

## Why this is the demonstration

A generic assistant asked "how do I build in Vietnam?" tends to produce a fluent, plausible procedure
with specific durations and steps — and the blinded baseline in `evals/results/2026-07-25-baseline.md`
showed exactly that failure on a comparable question, where the no-skill arm **asserted Chilean
procedural steps, a validity period and a fee basis as fact** and was marked FAIL.

The output above is deliberately less satisfying and considerably more useful. It separates:

- **structure** (transferable, and confidently stated),
- **physics** (universal, and stated without hedging because it needs none),
- **values and procedure** (local, dated, and explicitly flagged for confirmation).

That separation is the skill's central claim, and this is what it looks like when a builder actually
lands somewhere new.

> **Standing caveat.** This walkthrough is an illustration of method, assembled from secondary sources
> on 31 July 2026 — not Vietnamese construction advice. Every specific above needs confirmation against
> the current legal text and the actual authority before it reaches a programme or a number.
