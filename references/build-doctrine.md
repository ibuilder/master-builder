# Build Doctrine — How a Master Builder Builds Systems

Distilled from the working conventions (`CLAUDE.md`, roadmaps, and architecture) of real platforms
in the `ibuilder` org — Massing (IFC-native AEC platform), Voltra (validated trading engine), and
gcPanel/ConstructAI (construction PM). These are the transferable principles for building *anything* —
software, a data platform, a pro-forma engine, or a physical project — the way a master builder builds
a building. Read this whenever the task is to design, architect, validate, or ship a system or tool,
or to reason about *how* to build something reliably, not just *what*.

The through-line: **a master builder treats a codebase the way they treat a jobsite** — one source
of truth, stable identity, open interchange, staged validation, hard safety rails on irreversible
actions, and honesty about what is actually proven.

## Contents
1. Source-of-truth & stable identity
2. Do heavy work at the right layer; stream light artifacts
3. Open interchange over lock-in
4. Own your stack: offline-first, self-hostable, $0 to run
5. The staged-validation gate (never skip a stage)
6. Hard rails on irreversible actions
7. Honest status over optimistic status
8. Encode the domain: compliance-as-code
9. Modular by workflow; refactor toward maintainability
10. Operational discipline from day one
11. Applying the doctrine

---

## 1. Source-of-truth & stable identity

Massing's first non-negotiable: **IFC is the source of truth**, and every element is referenced by
its **IFC GlobalId (GUID), never by a transient viewer/session ID.** The lesson generalizes: pick one
canonical model of the data, and give every entity a stable identity that survives across tools, edits,
and time. In a pro forma it's the line-item ID; on a jobsite it's the drawing/spec reference an RFI cites;
in a cap table it's the SPV membership record. When identity is stable, everything else (issues, versions,
exports, audits) round-trips instead of drifting. **Identity drift is the root cause of most integration bugs.**

**And preserve the *why*, not just the *what*.** A stable record of the current state is half of it; the
other half is the constraint that produced it. Projects outlive the people who made their decisions —
staff turn over, consultants change, financing assumptions get revised — and the classic failure is a
team that inherits a choice, cannot reconstruct the reason for it, and either relitigates it at cost or
overturns it and rediscovers the original constraint the expensive way. (*Why is the column grid 8.4 m?
Why did we assume 10% vacancy?*) Record the decision, its owner, the alternatives rejected, and above
all **the constraint that drove it**, next to the thing itself: a note on the assumption in a model, the
RFI and change-order rationale on a job, the commit message and ADR in a codebase. Institutional memory
is infrastructure — and where it is missing, whatever holds the thread across time is worth more than
any single specialist.

## 2. Do heavy work at the right layer; stream light artifacts

Massing **pre-converts IFC to Fragments on the server and never parses full IFC in the browser at
runtime**; geometry streams as light `.frag`, metadata comes from the API — **geometry and data kept
separate.** The principle: put expensive, authoritative work where it belongs (server, batch, a solver)
and hand the client only what it needs, in the lightest form. The same instinct says: run the
interest-reserve circularity solver server-side and return the resolved schedule; don't push the whole
model to a phone. Match the work to the layer that can carry it.

## 3. Open interchange over lock-in

Issues (pins/RFIs/punchlist) follow the **BCF** model so they round-trip with other BIM tools; the
platform is **IFC-native, COBie-ready, IDS/BCF** throughout. The doctrine: prefer open, standardized
interchange formats at every boundary so data survives any single vendor and any single tool. Proprietary
formats are borrowed time. This is the software expression of the openness principle in `digital-toolkit.md`
and the reason the whole stack is MIT-licensed and self-hostable.

## 4. Own your stack: offline-first, self-hostable, $0 to run

"The viewer must run fully offline (local WASM, self-hosted tiles)"; Massing is "$0 to run," Voltra
ships a "free 24/7 deployment path (Oracle Always-Free + systemd)." Autodesk RVT is behind a paid,
feature-flagged bridge with an explicit cost warning — **never assume a proprietary dependency is
available.** Build so the core works on your own infrastructure with no mandatory paid dependency and
no phone-home. Ownership and resilience beat convenience you can't control.

## 5. The staged-validation gate (never skip a stage)

Voltra's central discipline: **backtest → walk-forward → Monte Carlo → 30-day dry-run → small live
capital — never skip a stage.** Hyperopt only on the training window; **always validate out-of-sample.**
The transferable idea is a gauntlet of increasingly-real tests that a thing must pass before it touches
consequences. For a building it's the estimate-class ladder (ROM → GMP) and the design phase gates; for
a pro forma it's base/downside/stress before you commit equity; for any model it's out-of-sample before
you trust it. **The most important milestone is usually not a feature — it's proving (or disproving) the edge.**
For anything *generated* — a layout, a frame, a detail — the gate must be **deterministic and physical,
not visual**: plausible-looking geometry is uncorrelated with buildable geometry
(`document-intelligence.md` §7).

## 6. Hard rails on irreversible actions

Voltra: **"NEVER set dry_run: false. Live config changes are human-only."** Every strategy must carry
1% risk sizing, on-exchange ATR stops, and drawdown/cooldown protections. Massing gates the
arbitrary-code escape hatch (sandboxed ifcopenshell / Bonsai-MCP: "runs arbitrary Python — gate it,
save first, chunk big ops"). The principle: **the step that can cause irreversible loss — moving real
money, executing arbitrary code, submitting a permit, pouring concrete — gets a human gate and a
safety rail, always.** Automate the reversible; require a human for the irreversible. This is the
software mirror of the professional-boundaries rule in SKILL.md.

## 7. Honest status over optimistic status

Voltra's README states plainly that the edge is **not yet statistically significant** (Monte Carlo
P(edge>0) = 81%, below the 95% bar) and runs paper-only. The doctrine: report what is actually proven,
label the estimate class, and never let a hopeful number masquerade as a validated one. This is the
same honesty as "a ROM is not a GMP" and "an entry cap is not an exit cap." Credibility compounds;
one oversold number spends it all.

## 8. Encode the domain: compliance-as-code

Massing turns code knowledge into software: **edition-aware occupancy-load + egress pre-check,
jurisdiction-adopted code editions, an approvability pre-flight, a detail-rule engine, and a
decision-readiness (RFI-prevention) audit** — plus **authoring guardrails that reject broken IFC at
creation.** The lesson: the highest-leverage tooling encodes the domain's rules so errors are caught
at authoring time, not in plan check or the field. Validate at the point of creation; make the invalid
state unrepresentable. (See `global-codes.md` for the domain rules being encoded.)

## 9. Modular by workflow; refactor toward maintainability

gcPanel/ConstructAI organizes strictly **by module mirroring the real construction workflow** —
Contracts, Cost, Engineering, Field, Reporting, Resources, Safety — each with a uniform list/form
(`Section`/`Form`) structure, and was explicitly refactored to push logic out of page files into
reusable components. Massing is a monorepo split by concern (`apps/`, `packages/`, `services/`,
`plugins/`, `integrations/`). Structure the system to match how the work is actually done, keep the
pattern uniform, and refactor toward maintainability as it grows.

## 10. Operational discipline from day one

Voltra shipped, before going live: TLS ingress, health monitoring + a dry-run tripwire, backups
**with a tested restore**, rate limiting, log rotation, CI, a trade/audit ledger, an incident runbook,
and key-rotation procedures. Build order starts with **smoke tests** and phases up. The doctrine: ops,
observability, backups-you've-actually-restored, and a rollback/incident plan are part of "done," not
a later chore. A building isn't finished at CofO and a system isn't finished at first deploy.

## 11. Applying the doctrine

When helping build or evaluate any system or tool, run these checks:
- What is the **single source of truth**, and does every entity have a **stable ID**?
- Is expensive work at the **right layer**, with light artifacts streamed out?
- Are all boundaries **open/standard formats**? Any hidden proprietary dependency?
- Can it run **on our own infra, offline, at low/zero cost**?
- What's the **validation gate**, and are we honest about which stage we're actually at?
- Where are the **irreversible actions**, and does each have a **human gate + safety rail**?
- Is the **status honestly labeled** (estimate class / significance / assumptions)?
- Are the **domain rules encoded** so bad states are caught at creation?
- Is it **modular by real workflow** and maintainable?
- Is **operational discipline** (tests, backups, rollback, runbook) part of "done"?

These are the same instincts that make a good jobsite — applied to whatever is being built.
