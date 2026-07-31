# Construction Delivery

How a project actually gets bought, built, sequenced, and controlled. Read this for delivery-method
selection, contracts, estimating, scheduling, procurement, and construction administration.

## Contents
1. Delivery methods (and when each fits)
2. Contract families (global)
3. Estimating — classes and drivers
4. Scheduling — CPM, pull planning, lookaheads, long-leads
5. Procurement, supply chain, and prefab/DfMA
6. Construction administration & controls
7. Quality, safety, and non-conformance
8. Tooling

---

## 1. Delivery methods (and when each fits)

The delivery method sets who holds which risk and when the price is known. Choose it to match the
owner's priorities among **cost certainty, speed, quality, and design control.**

> **Read the menu as a history, not a list.** Building was once delivered by a single accountable
> master builder holding design and construction together. That fragmented in the 18th–19th centuries —
> **an adaptation, not a fall**: formal architectural education, engineering as a discipline, and
> industrial-scale demand outgrew any one craft lineage, and specialization bought real technical depth.
> What it cost was integration. Design-bid-build separates design from construction, which externalizes
> the **coordination burden onto the owner** — usually the party least equipped to carry it — and sets up
> adversarial incentives when design assumptions meet field reality. Every method below is a different
> answer to the question *how much integration do we buy back, and who pays for it?* The market keeps
> answering "more": design-build is projected at **up to 47% of US non-residential construction spending
> in assessed segments in 2026** (DBIA/FMI), rising beyond that later in the decade. Choosing a delivery
> method is choosing where the seams will be — and seams are where projects fail.

- **Design-Bid-Build (DBB)** — design fully, then bid to a GC (usually low bid). Max design control,
  lowest collusion risk, but slowest and adversarial on changes. Common for public work.
- **Design-Build (DB)** — one entity for design + construction. Fast, single point of responsibility,
  fewer owner-side gaps; owner cedes some design control. Good for speed and clear programs.
- **Construction Manager at Risk (CMAR / CM/GC)** — CM joins in preconstruction for constructability
  and budgeting, then delivers under a **Guaranteed Maximum Price (GMP)**. Collaboration of DB with
  more owner design control. Common for complex institutional work.
- **Integrated Project Delivery (IPD)** — multiparty relational contract, shared risk/reward, shared
  BIM. Highest collaboration, best for complex projects with sophisticated owners.
- **EPC / turnkey** — Engineer-Procure-Construct, lump-sum, single accountability; dominant for
  industrial, energy, and infrastructure, and common internationally.
- **Public-Private Partnership (P3 / PPP)** — private finance + delivery + often operations (DBFO/M).
  For infrastructure and social assets; shifts lifecycle risk to the concessionaire.

Match to context: cost certainty + public accountability → DBB/GMP; speed → DB; complexity + owner
control → CMAR/IPD; infrastructure → EPC/P3.

---

## 2. Contract families (global)

Know the family; the clauses that fight are always the same: scope, price mechanism, time/EOT,
change/variation, payment, risk allocation, indemnity, LDs, dispute resolution.

- **AIA (US)** — A201 general conditions; A101/A102/A133 owner-contractor; B-series owner-architect.
- **ConsensusDocs (US)** — collaborative alternative to AIA.
- **FIDIC (international)** — the global standard for cross-border work: **Red** (build to employer's
  design), **Yellow** (design-build/plant), **Silver** (EPC/turnkey), **Green** (short form). Rainbow suite.
- **NEC4 (UK/international)** — collaborative, activity/option-based (Options A–F), proactive early-warning
  and programme management.
- **JCT (UK)** — traditional UK building contracts.

Internationally, FIDIC is usually the lingua franca; know which book matches the delivery method and
who carries design risk under it. The clause-by-clause fight over *who carries what* — site conditions,
delay and EOT, LDs, indemnity, and the insurance and bonds behind them — is in `risk-insurance.md`.

---

## 3. Estimating — classes and drivers

Never present an estimate without its **class** and basis; a ROM is not a bid. (AACE-style classes:)
- **Class 5 — ROM/order-of-magnitude** (concept): ±30–50%, from $/area or $/key.
- **Class 3 — budget/semi-detailed** (SD/DD): ±10–20%.
- **Class 1 — definitive / GMP / bid** (CDs): ±5–10%, quantity-take-off + priced subs.

Cost drivers to interrogate: location cost index (labor + material), building type/complexity,
structural system, floor-to-floor and façade ratio, site & foundations (the great cost wildcard),
MEP intensity, finishes level, schedule (acceleration costs money; so does carry), market conditions
(escalation), and procurement route. Always carry **escalation** and a **contingency** sized to the
design maturity and risk. State currency + date on every number.

> **The 2025–26 escalation environment is a live driver, not a background assumption.** US **Section 232
> tariffs of ~50% on steel, aluminium, and copper** (derivatives ~25%) pushed steel mill products up
> ~20% and aluminium ~33% year-over-year into early 2026, with pressure sustained by data-centre,
> electrification and advanced-manufacturing demand.
>
> **Name the index, and check it yourself — the published indices disagree, materially.** As of
> **Q1 2026**, Mortenson's nonresidential index ran **+1.69% on the quarter and +6.77% year-over-year**
> (materials +7.0%, trade-partner work +6.6%), while Turner's was **+1.3% on the quarter and +3.1%
> against the 2025 average** — a spread wide enough to change a go/no-go on a long programme. They
> differ by basket, geography, and whether they track bid prices or input costs. So **"construction
> escalation is X%" is not a fact until you say whose index, which quarter, and which market**; pick the
> index that matches your project type and location, quote it with its date, and re-check it at estimate
> time rather than carrying a number forward. Treat metals, and anything
> imported, as volatile: get **firm quotes with expiry dates**, negotiate **price-escalation / material-cost
> clauses** (who carries the tariff and commodity risk — the allocation question, and the clauses that
> settle it, are in `risk-insurance.md` §3), buy out and lock long-leads early, and carry
> escalation explicitly rather than burying it. In the EU, **CBAM** now adds a carbon cost to imported
> steel/cement/aluminium (see `sustainability-carbon.md`). Confirm current tariff and commodity levels at
> estimate time — they move on policy, not on cycles.

---

## 4. Scheduling — CPM, pull planning, lookaheads, long-leads

- **CPM (Critical Path Method)** — the master schedule; the **critical path** is the chain with zero
  float that sets the finish date. Manage float, not just activities; protect the critical path.
- **Last Planner / pull planning** — the lean field method: the crews who do the work plan backward
  from milestones, make ready by removing constraints, and commit to weekly work plans. Measured by
  **PPC (Percent Plan Complete)**. Massing includes a Last Planner board for exactly this.
- **Lookaheads** — the rolling **4–6 week** (and 1-month) windows that turn the master schedule into
  actionable constraint-removal; the workhorse of field coordination.
- **Long-lead procurement** — the schedule killer. Switchgear, generators, elevators, chillers,
  curtain wall, structural steel, custom AHUs can carry many-month or year-plus lead times. Electrical
  gear has blown out: as of 2026 **large power transformers run 2–4 years** and switchgear is measured
  in quarters — for power-intensive projects the electrical infrastructure, not the structure, is
  frequently the critical path (see the interconnection gate in `global-codes.md` §2). Maintain a
  **long-lead expediting log** and release these early — often before CDs are complete. (This is a
  deliverable Matt has produced on live projects.)


### Delay analysis — how you prove it, not just assert it

When the job runs late, "who caused it" stops being a conversation and becomes an evidentiary exercise.
Two published frameworks govern, and they are **complementary rather than competing**: the **SCL Delay
and Disruption Protocol (2nd edition)** and **AACE International RP 29R-03, Forensic Schedule
Analysis**, which sets out nine methodologies. Name the one you are using and why — an unnamed method
is the first thing the other side attacks.

**Classify the delay before you measure it.** Three questions, in order, and they are independent:

1. **Excusable?** Was the cause outside the contractor's control (owner change, design error, differing
   site conditions, permit delay, exceptional weather, force majeure)? If not, it is **non-excusable** —
   the contractor absorbs it and may owe LDs.
2. **Compensable?** Excusable buys *time*. Money is a separate question: owner-caused delay is normally
   **excusable and compensable** (prolongation costs follow); neutral events like weather are usually
   **excusable but non-compensable** — time, no money. Conflating the two is the most common and most
   expensive error in this whole area.
3. **On the critical path?** A delay to an activity with float consumes float, not time. **Whoever owns
   the float matters** — many contracts are silent, and "float belongs to the project" versus "to the
   contractor" changes the answer. Check the clause before you argue.

**Concurrent delay** — two independent causes, one owner-side and one contractor-side, driving the same
period — is where most disputes actually live, and the treatment is jurisdiction- and contract-specific.
Get it advised, not assumed.

**The method families** (AACE groups them by observational vs modelled, static vs dynamic, additive vs
subtractive):

| Method | What it does | Best for |
|---|---|---|
| **As-planned vs as-built** | Compares the baseline to what happened | Simple, cheap, weakest evidentially |
| **Windows / contemporaneous period analysis** | Walks the schedule period by period using the updates as they were | The most defensible, and usually preferred where updates exist |
| **Impacted as-planned** | Inserts delay events into the baseline | Prospective EOT; ignores what actually happened |
| **Time impact analysis (TIA)** | Models a single event against the schedule current at that moment | Contemporaneous EOT applications — often what the contract requires |
| **Collapsed as-built ("but-for")** | Removes delays from the as-built to show what would have happened | Retrospective claims; contentious, sensitive to assumptions |

**What actually decides these cases is records, not method.** Contemporaneous, dated evidence —
schedule updates, daily reports, weather logs, correspondence, and above all **notice given on time** —
beats a sophisticated analysis built after the fact. Most delay disputes are notice disputes. Keep an
updated CPM throughout, not a baseline you stopped maintaining at month three.

> Delay entitlement is contractual and jurisdictional. Reason through the classification and the method
> here, then route the claim itself to a scheduling expert and construction counsel — the standards
> above set out the technique, and the specific clause and forum set the outcome.
> (Allocation and the EOT/compensability clauses: `risk-insurance.md` §3.)

---


## 5. Procurement, supply chain, and prefab/DfMA

- **Buy-out** — converting the estimate into awarded subcontracts and POs; scope-gap analysis is
  where budgets are won or lost.
- **Prefabrication / modular / DfMA (Design for Manufacture and Assembly)** — move work off the
  critical path and into a controlled factory: volumetric modules, panelized façades, MEP racks,
  bathroom pods. Trades speed, quality, and site-labor risk for early design lock and transport/
  logistics constraints. Increasingly essential where site labor is scarce or expensive.
- **Global supply chain** — lead times, tariffs, currency, and logistics belong in the schedule and
  the estimate, not as an afterthought — especially for cross-border projects.

---

## 6. Construction administration & controls

The daily machinery of building. Each artifact is both a communication and a contractual record:

- **RFI (Request for Information)** — formal question to the design team to resolve a gap/conflict.
  Good RFIs are specific, cite the document, propose a resolution, and flag cost/schedule impact.
- **Submittals** — shop drawings, product data, and samples the contractor submits for the design
  team to review against the contract documents before fabrication/installation. Track against the
  schedule; a late submittal is a late long-lead is a late project.
- **Change management** — change events → potential change orders → **change orders (COs)**, each with
  cost + time impact; track **change-event cost exposure** against contingency.
  **Auditing a priced CO (owner side)** is a distinct skill and normally an hour or more of PM time per
  change. Four checks, in order of how reliably they find money:
  1. **Markup / O&P / bond caps** — is the applied markup within the contract's cap, and is it
     **stacked**? Overhead-and-profit taken again at each tier (sub → sub-sub → GC), or a bond/insurance
     percentage applied on top of a marked-up base, quietly compounds. Check the contract exhibit.
  2. **Unit-price inflation** — line rates against the contract's rate schedule or the awarded bid tab.
     Rates that were competitive at bid often are not in a change.
  3. **Labor-rate padding** — billed rates and classifications against the agreed labor-rate schedule
     (and, on T&M tickets, whether the classification billed matches the work performed).
  4. **Quantity tie-out** — claimed quantities against the drawing set or an independent takeoff.
  Recompute every extension from quantity × rate rather than trusting a printed total, and report each
  finding as *a dollar amount with a page reference*. Distinguish arithmetic findings (assertable) from
  judgment ("is 42 hours reasonable?" — surface it, don't rule on it). The method, and the extraction
  traps that make naive checking produce false positives, are in `document-intelligence.md`.
- **Payment applications** — **AIA G702/G703** (or local equivalent): the schedule of values, percent
  complete, stored materials, and retainage that drive the monthly draw. Ties directly to the lender
  draw (finance ref §5).
- **Coordination** — clash resolution and action items from the coordinated model / BCF (see
  `digital-toolkit.md`); resolve in the model, not in the field.
- **Cost & schedule controls** — earned value where warranted, budget vs. committed vs. forecast,
  and the lookahead as the operating rhythm.

These are exactly the workflows Matt's tools automate (RFI draft generation, submittal-log analysis,
Procore submittal-date automation via API/Selenium, pay-app generation) — reach for them to do the
work, not just describe it.

---

## 7. Quality, safety, and non-conformance

- **QA/QC** — QA is the system (procedures, ITPs, inspections); QC is the checking of the work.
  Benchmark mock-ups and first-of-kind inspections catch systemic defects early.
- **Non-Conformance Reports (NCRs)** and formal notices — document defective/nonconforming work,
  the disposition (rework/repair/accept-by-concession), and prevention. A paper trail that protects
  the project.
- **Safety** — the non-negotiable. OSHA (US, incl. OSHA 30), CDM Regulations (UK), local equivalents.
  Safety is a leading indicator of a well-run job; a chaotic site is an unsafe site and usually a
  late one. Design for safety and constructability, plan the high-risk sequences, and never let
  schedule pressure erode it.

---

## 8. Tooling

To run the work rather than just narrate it, prefer interoperable platforms and reach for the ones
already built:
- **Massing** GC portal (near-100 modules), 5D cost/schedule, ISO 19650 CDE, CPM schedule, TRIR
  safety tracking, Facility Condition Assessment — the integrated command layer on one IFC-keyed model.
- **FieldForge** — pay-per-use RFI Draft Generator and Submittals Log Analyzer for mid-size GCs.
- **gcPanel / ConstructAI** — Next.js + TypeScript + Tailwind construction-management dashboard,
  modular by real workflow (Contracts, Cost, Engineering, Field, Reporting, Resources, Safety) with a
  uniform list/form component structure.
- **Procore** and BuildingConnected in the commercial ecosystem; automate the repetitive workflow via
  their APIs.

Match the tool to the control it serves, and keep the data in open formats so it survives the project.
