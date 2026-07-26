# Risk, Insurance & Surety

Step 7 of the protocol, in depth. Every other reference tells you how to *do* something; this one tells
you who carries it when it goes wrong. Read this for risk registers, contractual risk allocation,
insurance products, bonds, contingency sizing, and the increasingly hard question of whether a project
is **insurable at all**.

The master builder's discipline: **a risk that has not been named, priced, and assigned to someone is
carried by the owner by default.** Silence is an allocation — usually the worst one.

## Contents
1. The risk loop, and the allocation principle
2. The risk register
3. Contractual allocation — the clauses that actually fight
4. Insurance — the products and what each really covers
5. Surety — bonds are not insurance
6. The 2026 market, and the insurability problem
7. Contingency is risk capital
8. Universal vs local

---

## 1. The risk loop, and the allocation principle

Run it in order, and keep running it — a risk register written at feasibility and never reopened is a
document, not a control.

1. **Identify** — name the risk in concrete terms. "Market risk" is not a risk; "absorption slower than
   12 units/month at the underwritten rent" is.
2. **Assess** — likelihood × impact, in money and in time. Rank. Most registers have 3–5 that matter.
3. **Allocate** — decide *who carries it*, via contract, insurance, bond, or contingency.
4. **Mitigate** — reduce what remains through design, sequencing, procurement, or phasing.
5. **Monitor** — assign an owner and a trigger. A risk with no named owner is unmanaged.

> **The allocation principle: give each risk to the party best able to control, price, and absorb it.**
> All three. A subcontractor may *control* a risk but be unable to *absorb* it — pushing it down just
> converts a construction risk into a counterparty-insolvency risk, and you get it back with a claim
> attached. Risk pushed onto a party that cannot carry it is not transferred; it is disguised.

The corollary developers forget: **risk transfer is never free.** A contractor asked to swallow
unquantifiable risk prices it — or prices it *badly*, which is worse, because a bid that ignores a real
risk becomes a change order or a dispute later.

---

## 2. The risk register

The feasibility deliverable (`development-lifecycle.md` §5) and a living document thereafter. Cover, at
minimum, these families — each with an owner, a mitigation, and a trigger:

- **Entitlement** — approval refused, conditioned, appealed, or simply *late*. Usually the longest pole
  and the hardest to insure. Mitigate with option/contingency structures, not optimism.
- **Site & ground** — soils, groundwater, contamination, archaeology, unforeseen conditions. The classic
  cost wildcard; who carries "differing site conditions" is a contract question (§3).
- **Design** — incomplete/coordination errors, late changes, scope gaps at buy-out.
- **Cost** — escalation, tariffs, commodity moves, bid-market conditions (`construction-delivery.md` §3).
- **Schedule** — long-leads, utility interconnection, weather, labor availability, permit/inspection pace.
- **Counterparty** — contractor or key-sub insolvency, partner default, tenant credit.
- **Capital & market** — interest-rate moves, refinancing/take-out risk, absorption, exit-cap movement.
- **Physical & climate** — flood, wind, wildfire, seismic, extreme heat (`sustainability-carbon.md` §7).
- **Regulatory & transition** — code cycle changes, carbon/energy mandates, tax and policy shifts.
- **Force majeure** — the genuinely uncontrollable; note that it usually buys *time*, not *money*.

---

## 3. Contractual allocation — the clauses that actually fight

The contract is the primary risk-allocation instrument; insurance is the backstop behind it. In every
contract family (AIA, FIDIC, NEC, JCT — `construction-delivery.md` §2), the same handful of clauses
decide who loses money when things go wrong:

- **Differing / unforeseen site conditions** — does the owner or the contractor carry the ground? FIDIC
  Red and most owner-design forms leave much of it with the owner; EPC/Silver pushes it to the
  contractor (and the price reflects that).
- **Change / variation** — what counts as a change, how it's valued, and the notice period. Most
  disputes are notice disputes.
- **Time, EOT, and concurrent delay** — extension of time vs. *money*. A contractor may win time and
  still absorb its own prolongation cost, depending on whether the delay is excusable *and*
  compensable. Know which delays are which before you sign — and know **who owns the float**, because
  a delay that only eats float is not a delay to completion. How entitlement is actually *proved* —
  the SCL Protocol and AACE 29R-03 method families, and why records beat method — is in
  `construction-delivery.md` §4.
- **Liquidated damages (LDs)** — the owner's pre-agreed delay remedy. Must be a genuine pre-estimate of
  loss, not a penalty, or it may be unenforceable. Usually capped; the cap is the real negotiation.
- **Indemnity & limitation of liability** — who defends whom, and the overall liability cap (often a
  percentage of contract value). Watch for consequential-damages waivers — they can quietly exclude the
  losses the owner actually cares about (lost rent, financing costs).
- **Waiver of subrogation** — stops one project party's insurer suing another. Standard, important, and
  routinely deleted by accident.
- **Retention / retainage** — typically 5–10%, released at substantial completion and after defects.
- **Defects liability / DLP & warranties** — the tail after handover, and who holds it.
- **Dispute resolution** — negotiation → mediation/DAB → arbitration/litigation, and the *seat*. On
  cross-border work this is a commercial decision, not boilerplate.

> Contracts are legal instruments. Reason about the allocation and its commercial consequence, then
> route the drafting and the final position to **qualified construction counsel** in the project's
> jurisdiction. (Professional boundaries, per SKILL.md.)

---

## 4. Insurance — the products and what each really covers

Match the product to the phase and the peril. Naming the right policy is half of a builder's
credibility in a risk conversation.

- **Builder's Risk / Contractors' All Risks (CAR)** — property damage to the *work in progress*, plus
  materials in transit and stored off-site if endorsed. First-party. The critical extensions are
  **delay in start-up / advance loss of profits (DSU/ALOP)** — which covers the *financing and revenue*
  consequence of a covered loss, not just the rebuild — plus **soft costs** and **testing/commissioning**.
  Watch flood/quake/wind sub-limits and deductibles: in CAT zones the sub-limit, not the policy limit,
  is your real cover.
- **Commercial General Liability (CGL)** — third-party bodily injury and property damage. Check
  completed-operations and the **contractual liability** grant that backs your indemnities.
- **Professional Indemnity / Errors & Omissions** — design negligence. Carried by designers; under
  **design-build** the contractor needs it too, and owners should verify the **project-specific** limit
  rather than a firm-wide one already eroded by other claims.
- **Workers' compensation / employers' liability** — statutory and non-negotiable.
- **Environmental / pollution legal liability** — essential on brownfield and adaptive reuse (asbestos,
  lead, contaminated soil — see the reuse reference).
- **Wrap-ups — OCIP / CCIP** (owner- or contractor-controlled insurance programs) — one policy covering
  all enrolled parties on a large project. Buys consistent limits, removes cross-litigation, and can
  save cost at scale; costs administrative overhead and careful enrollment/audit discipline.
- **Subcontractor default insurance (SDI, e.g. "Subguard")** — the contractor's alternative to
  requiring subcontractor bonds; faster to trigger, but it is *the contractor's* asset and carries a
  deductible and co-pay the owner should understand.
- **Title, and rep-and-warranty insurance** — on the transaction side.
- **Existing-structure property** — on renovation, the *existing building* is usually covered by the
  owner's property policy, not builder's risk. The seam between the two policies is a classic gap;
  close it deliberately.

---

## 5. Surety — bonds are not insurance

A frequently muddled distinction, and it matters commercially:

- **Insurance** is a two-party risk-transfer: you pay a premium, the insurer expects losses and pays them.
- **A surety bond** is a three-party guarantee (principal, obligee, surety) that the principal will
  perform. The surety expects **zero** losses and, if it pays, it **seeks indemnity back from the
  contractor.** A bond is underwritten credit, not risk transfer.

The instruments:
- **Performance bond** — guarantees completion if the contractor defaults (commonly 100% of contract value).
- **Payment / labour-and-material bond** — protects subs and suppliers, and therefore protects the owner
  from liens.
- **Bid bond**, **advance-payment**, **retention**, and **warranty/maintenance bonds** for their phases.
- **Parent-company guarantee** — sometimes offered instead; only as good as the parent's balance sheet.

**Bonding capacity is a real constraint.** A contractor's surety limits both single-project and
aggregate exposure — a bidder can be technically excellent and simply unbondable at your project's size.
Test it during prequalification, not at award. Internationally, on-demand bank guarantees are common
instead of conditional surety bonds; they behave very differently when called.

---

## 6. The 2026 market, and the insurability problem

Insurance has moved from a line item to a **feasibility variable** — in some places it decides whether
a project happens at all. The current picture (verify at underwriting; this market moves fast):

- **A split market.** Builder's risk has broadly stabilized — single-layer programs seeing roughly
  **5–7% decreases in non-catastrophe zones** — while **catastrophe-exposed placements ran up ~12%**,
  and general contractors' overall insurance costs rose sharply (reports of ~22% in 2026). Where the
  project sits matters more than what it is.
- **Severe convective storm is the dominant peril, not hurricane.** US insured losses from hail,
  tornado, and straight-line wind exceeded **$51bn in 2025** — a third consecutive year above $50bn and
  more than any other natural-catastrophe category. This reprices ordinary inland markets that used to
  be considered benign.
- **Combustible construction is hardest to place.** Wood-frame builder's risk remains constrained on
  fire and weather exposure, though capacity is returning as London markets re-enter.
- **Ballpark only:** small residential/light commercial builder's risk often lands somewhere around
  **1–5% of construction value** — a range so wide it is useful only as a sanity check. Get a real quote
  early; on a CAT-exposed or frame project, insurance can move the pro forma.

> **Underwrite insurability, not just insurance cost.** In wildfire, coastal-wind, and flood-exposed
> markets, the live questions are whether cover is *available*, at what **deductible and sub-limit**, and
> whether the **operating** policy at stabilization will still be affordable — an asset that cannot be
> insured cannot be financed or sold. Rising premiums also hit **NOI directly** (an OpEx line), so they
> compress value at the exit cap. This is where physical climate risk stops being an ESG topic and
> becomes a valuation input (`sustainability-carbon.md` §7): **resilience measures are increasingly
> underwritten and credited**, so hardening the building is partly an insurance-cost play.

Insurance placement is a **licensed broker's** work, and policy wordings decide coverage. Reason about
what must be covered and who carries it; route the placement, wording, and certificates to a
construction-specialist broker and counsel.

---

## 7. Contingency is risk capital

Contingency is not padding; it is the retained portion of the risk register — the risks you decided to
carry rather than transfer. Size it to *risk and design maturity*, not to a habit:

- **Design/development contingency** — held by the owner, shrinking as the design matures (generous at
  concept, small at CDs). Tied to estimate class (`construction-delivery.md` §3).
- **Construction contingency** — for what emerges in the field; on adaptive reuse it should be visibly
  larger because unknowns live behind finishes.
- **Escalation** — a forecast, not a contingency. Carry it as its own line.
- **Owner's reserve / interest reserve** — schedule slip costs carry (`real-estate-finance.md` §5).

A useful discipline: **tie the contingency draw to the register.** When a contingency is spent, name the
risk it retired. A contingency that drains without any risk closing is really an estimating error, and
you want to learn that early, not at 80% complete.

---

## 8. Universal vs local

**Universal:** the risk loop, the allocation principle, the difference between a bond and a policy, the
logic of contingency, and the clause families that fight. These travel to every jurisdiction.

**Local and requiring verification:** compulsory cover (workers' comp/employers' liability, decennial
liability in France/Spain and much of the civil-law world, inherent-defects insurance in the UK),
statutory bond requirements on public work (US Miller Act and state "Little Miller" acts), enforceability
of LDs and indemnities, lien rights, and the entire pricing environment. Get local broker and counsel
input before treating any of the numbers or structures above as settled.
