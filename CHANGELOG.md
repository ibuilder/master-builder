# Changelog

All notable changes to the **master-builder** skill.

## [0.3.0] — 2026-07-21
Currency + decarbonization pass. Adds carbon as a first-class development discipline, refreshes code
editions to mid-2026, and folds in the power-constrained and tariff-driven cost environment.

### Added
- `references/sustainability-carbon.md` — whole-life & embodied carbon: the EN 15978 module map, the
  accounting standards (EN 15804 EPDs, RICS WLCA 2nd ed, ISO 14040/44), the 2026 regulatory teeth
  (EU CBAM definitive period, EPBD, Buy Clean, LEED v5 embodied-carbon prerequisite, ICC 2027 carbon
  focus), carbon-is-money (CBAM cost, green premium/brown discount, transition/stranded-asset risk),
  the reduction hierarchy, and a hotspot/cost-concentration method.

### Changed
- SKILL.md — ground-in-place rule now derives **power** (interconnection queue) and **carbon** from
  location; carbon reference added to the protocol and the reference table; carbon-boundary output
  convention added; `description` extended to trigger on carbon, decarbonization, and power/data-center questions.
- `global-codes.md` — utility-service gate sharpened to the 2026 power reality (~2,600 GW US
  interconnection queue, PJM 8-year application-to-operation, transformer 2–4-year lead); ICC 2027 and
  second-generation Eurocode timelines (definitive 2026 / publish 2027 / withdraw 2028) made concrete;
  carbon added to the energy/sustainability stack and the editions note.
- `digital-toolkit.md` — ISO 19650 second-generation revision (DIS 10 Mar 2026, BIM→IM, unified 9-step
  process, final 2027); 5D take-off feeds whole-life carbon; embodied-carbon row added to the software map.
- `construction-delivery.md` — 2025–26 escalation/tariff environment (Section 232 ~50% metals tariffs,
  ~8% aggregate escalation, price-escalation clauses) added to estimating; transformer/switchgear lead
  times added to long-leads.
- `real-estate-finance.md` — escalation/tariff and carbon (CBAM, green premium/brown discount,
  transition risk) added to the common-traps list.

## [0.2.0] — 2026-07-20
Enrichment pass after grounding on real projects and a live feasibility test (a retail-to-vertical-farm
development thesis and its pro-forma model).

### Added
- `references/build-doctrine.md` — cross-cutting engineering lessons distilled from real platforms
  (source-of-truth & stable identity, do heavy work at the right layer, open interchange, staged-
  validation gate, hard rails on irreversible actions, honest status, compliance-as-code).
- `references/pro-forma-review.md` — forensic model/deal review: reframe the asset, reconciliation pass,
  a defect checklist (NOI gross-up, dropped cost lines, non-cash in OpEx, zero-vacancy, unit errors),
  the three-questions test for assumptions, cost-concentration analysis, and validate-demand-before-capital.

### Changed
- SKILL.md protocol now leads program analysis with "name what the asset actually is" (reframe first).
- `global-codes.md` — utility interconnection / will-serve added as a schedule-and-cost gate for
  energy- and water-intensive uses and on-site generation.
- `digital-toolkit.md` and `construction-delivery.md` corrected to the verified architecture of the
  real repos (Massing on That Open Fragments + IfcOpenShell with GUID-stable server-side edit recipes,
  three pillars Model/Construction/Finance, code-intelligence pre-checks; gcPanel/ConstructAI on Next.js/TS).

## [0.1.0] — 2026-07-20
Initial release.

### Added
- SKILL.md — the Master Builder Protocol, ground-in-place rule, professional boundaries, output conventions.
- References: `global-codes.md`, `development-lifecycle.md`, `real-estate-finance.md`,
  `construction-delivery.md`, `digital-toolkit.md`.
