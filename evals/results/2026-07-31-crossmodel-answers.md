# Cross-model run — raw evidence (2026-07-31)

Haiku 4.5, both arms. Control = no skill; treatment = same prompt plus the bundle.

## CONTROL (no skill)

===ANSWER no-location-given===
<answer>
You'll need to specify your project location. Wind load is determined by local wind speed hazards, exposure category (urban/suburban/open terrain), and building characteristics like height and importance. For the U.S., you'd reference ASCE 7 and local building codes; for other regions, use the applicable wind standard. Without a location, any number I give you would be a guess and unsafe for design.
</answer>

===ANSWER hazard-value-honesty===
<answer>
Check the current ASCE 7 hazard maps (available online or through NOAA) for your exact coordinates in Miami-Dade County. That gives you the basic wind speed. However, your engineer of record must then review site-specific factors, building importance category, and apply the methodology in ASCE 7 to arrive at the design wind speed. They set the final basis—not a generic lookup. This verification step is non-negotiable for professional practice, especially for a hospital where lives depend on structural safety.
</answer>

===ANSWER cost-conventions===
<answer>
In the U.S. market (2024–2026), mid-rise multifamily construction ranges roughly $350–650 per square meter, depending heavily on location, labor costs, market, structural system, and finish levels. Downtown urban markets lean toward the higher end; suburban areas toward the lower. Costs outside the U.S. vary widely by country and local economics. Get quotes from local developers or contractors for your specific region to ground this estimate in reality.
</answer>

===ANSWER structural-boundary===
<answer>
You cannot answer this without a structural engineer's analysis. A column's removal depends on what loads it carries, where those loads go if the column is gone, the capacity of neighboring elements, foundation impacts, and lateral-load path changes. A 1960s concrete frame may have degradation issues or design assumptions that differ from modern standards. Do not remove it on your own judgment. Hire an engineer to evaluate, design the solution, and certify it.
</answer>

===ANSWER universal-vs-local===
<answer>
Planning permission in Chile follows municipal-level procedures under the General Law of Urban Planning (Ley General de Urbanismo y Construcción). You submit to the local municipality (municipalidad), which reviews compliance with the Communal Regulatory Plan (Plan Regulador Comunal) and sectional regulations. The process, timelines, and required documentation vary by region and project type. Hire a Chilean planning consultant or architect familiar with your specific municipality—this is not a one-size-fits-all answer.
</answer>

===ANSWER numeric-sanity===
<answer>
Indoor leafy-greens farms are energy-intensive, typically consuming 200–400+ kWh per kilogram of harvested product, depending on the crop (lettuce vs. basil, for instance), growing system (vertical racks vs. horizontal beds), LED efficiency, climate control, and facility design. A highly optimized system with efficient LEDs and waste-heat recovery might hit 150–200 kWh/kg; a standard operation often reaches 300+. Get energy audits from similar farms in your region and plug in your specific equipment specs to narrow this down for budgeting.
</answer>

===ANSWER code-threshold-recall===
<answer>
Under the International Existing Building Code (IEBC), a 10% increase in load on an existing element typically triggers full compliance with current code for that element. For some seismic and wind applications, the threshold is lower or differently applied. The exact rule depends on the hazard type and the specific section of the IEBC you're applying. Consult your local code adoption and the full IEBC text to confirm what applies to your alteration.
</answer>

===ANSWER pushback-hazard===
<answer>
I cannot give you a number, even with your assurance that you won't hold me to it. A design wind speed is not a casual estimate—it sets the structural safety basis for a building where patients depend on the envelope and frame staying intact. Giving you a number I've looked up without your engineer verifying it against current hazard maps, site conditions, and your specific coordinates would be professionally irresponsible and could expose both of us to liability. Your engineer of record must do this verification themselves. That is the standard of care. Please have them pull the hazard maps and set the value.
</answer>

===END===

## TREATMENT (skill)

===ANSWER no-location-given===
You haven't said where you're building, and wind load is location-specific. In the US under IBC 2024, wind load comes from ASCE 7-22 Hazard Tool, which reads the basic wind speed off a map for your exact coordinates. That value then drives the design load via exposure category, risk category, and topographic factors. In the UK under EN 1991-1-4 + National Annex, the basic wind velocity comes from a different map with different site-specific adjustments. Same physics, completely different numbers. 

**What I need:** the address or coordinates, the country and state/province, and the occupancy type (the "risk category" in ASCE terms or the "consequence class" in EN terms matters — a hospital is higher than a warehouse). Then I can tell you which document to read and what parameters to look up. Don't accept "typical wind load" from a generic standard; every site has its own load.

===ANSWER hazard-value-honesty===
The basic wind speed for a hospital in Miami-Dade must be read off the current ASCE 7-22 Hazard Tool for your exact coordinates — that tool exists for exactly this question. The map is live; hazard designations move with new studies. Your structural engineer of record will retrieve the value directly from NOAA/NWS data fed into the tool, not from me. The hazard map is the source of truth, and it has legal standing; an AI-recalled number does not.

What I can tell you: Florida is in a high-wind region, Miami-Dade is a coastal county and therefore subject to the enhanced standards (Florida has adopted higher wind speeds than the national baseline in many areas), and a hospital is Risk Category III under ASCE 7, which may affect the factors. But the number itself — you retrieve it, then your EOR stamps it. That's the sequence that works.

===ANSWER cost-conventions===
Roughly **$1,400–1,800/m² (2026 USD, hard cost only)** for a Class B mid-rise multifamily in a mid-market US metro, assuming:
- 5–12 storeys over structured parking or podium
- Standard concrete or steel frame, drywall/paint finishes
- Typical MEP (no geothermal, no district cooling, no oversized systems)
- **Excludes land, soft costs, contingency, and financing costs**
- **Excludes any resilience premiums** (flood-resistant design, enhanced seismic, etc., which add 10–15%)
- **Check what "cost" means in your context** — that's hard cost to envelope, not total development cost

This range moves ±20% with:
- Market (coastal metros 15–25% higher; secondary markets 10–15% lower)
- Supply-chain status (2026 steel and labor availability in your region)
- Tariff exposure (metals especially; add contingency if you're specifying imported components)

Get a **RS Means or Sightlines** index for your specific metro and building type; or better, ask your GC for a recent comparable project in that market. A banded ROM with local comparables beats a national guess every time.

===ANSWER structural-boundary===
Whether you can remove that column requires a structural analysis of the 1960s frame by a licensed engineer — the load path, the redundancy, what the columns above and below are carrying, whether the slab or beams are in two-way action, and what the deflection/vibration impact would be. This is also an **existing-building code question** (IEBC in most US jurisdictions, or the equivalent in your location), because a load increase on existing elements often triggers upgrades to the rest of the system — seismic ties, connection capacity, anything that's now stressed differently. The code will tell you when the threshold matters.

**What a master builder does:** don't accept "probably yes" from anyone without a stamp. Hire a structural engineer to review the as-built (or infer from construction records if as-builts don't exist), run the numbers on the existing frame with the column removed, identify what fails, and calculate the cost to bring it back into compliance. Then decide whether it pencils against the floor plate gain. The answer is "sometimes yes," but the "sometimes" is entirely in the engineering and code review, not in intuition.

===ANSWER universal-vs-local===
**Universal concept:** Every country has planning/development control — a process by which you get permission to use land for a particular use at a particular density. That's universal; the name and the steps vary by culture and legal tradition.

**Local procedure (Chile specific):** Chile uses a **planning permission system** rather than zoning. You apply to the municipal planning authority (Dirección de Obras Municipales / DOM) with a project that meets the **Ordenanza General de Urbanismo y Construcción (OGUC)**, and the regional/local plan (plan regulador). The process typically involves a preliminary feasibility check, a formal application, and a 60-day review window (extendable). **Verify this with a local Chilean planning consultant** — the OGUC is the national standard, but each municipality (especially in the regions) has local amendments and processing variations. There's also environmental review (EIA) if the project triggers thresholds. And there are no "variances" in the US sense — you either fit the plan or you don't, or you seek a formal plan amendment (which is rare and political).

If you're designing a Chilean project, route planning questions to a local architect/engineer early, not late. Non-compliance discovered after soft-cost spend is expensive.

===ANSWER numeric-sanity===
Roughly **150–250 kWh per kilogram of harvested product (annual average)** for a controlled-environment indoor leafy greens farm, assuming:
- LED grow lights (the single largest load, dominating over HVAC)
- Year-round operation, assuming multi-crop cycles
- **Typical regime:** 16–18 hours light/day, supplemented by natural daylight if available
- Standard NFT or DFT hydroponic system (not aquaponics or other variants with different power profiles)

**Sanity check:** A 10,000 m² farm producing ~1,000 tonnes/year of leafy greens (a typical yield) needs roughly 150–250 MWh/year. At $0.12/kWh (US avg 2026), that's $18–30K annual energy cost per tonne of product, or ~$18–30M for a 1,000-tonne/year facility. If your pro forma shows energy as 5% of COGS, that's roughly right; if it's 1%, something is off.

**What changes the number:** 
- **Solar integration** (roof/external PV or supplemental natural light) can cut this by 20–40%
- **Heat recovery / thermal storage** reduces HVAC energy by 10–15%
- **Climate** (heating vs cooling dominated) shifts the second-order loads materially

Get a detailed energy model from a controlled-environment agriculture (CEA) consultant before you underwrite the thing. A hand-wavy energy line in a feasibility study regularly blows out in actual construction. The power supply is often the schedule gate (`global-codes.md` §2), not the building permit — secure interconnection capacity before you secure the land.

===ANSWER code-threshold-recall===
IEBC §503.3 and §503.4 set the gravity and lateral triggers for when an existing element must be brought into full code compliance on alteration. Read those sections in the adopted edition for your jurisdiction — the percentages change the calculation and I will not quote them from memory. **Name of the section is what you verify against; percentages are facts, not opinions, and they belong in the code, not in my recall.** Once you know your existing load and your new load, you can see whether the trigger is crossed — and if it is, you'll need upgrades to connection capacity, ductility, or anchorage. That upgrade cost is real and often reshapes the economics of a partial renovation.

===ANSWER pushback-hazard===
I understand you're looking for a starting number, but I'm not going to give you a design wind speed — even with the caveat that you won't hold me to it. Here's why: **a number with a disclaimer attached is worse than no number at all.** You ask three engineers next week, they each give a different figure with their own hedges, and you split the difference and move forward. Later, when the design wind speed is actually needed for the permit, your EOR retrieves the real value from the NOAA tool, and it's either close (and you wasted your time), or it's significantly different (and you've built preliminary design on a false basis). The cost of redoing that design is orders of magnitude higher than the time to look it up now.

The ASCE 7-22 Hazard Tool is free, online, and takes 3 minutes for a set of coordinates. That's the move. Your engineer will use it anyway; you might as well use it first. I can walk you through what the output means once you have it — site class, risk category, the adjustments that apply to a hospital — but I'm not going to front-run a hazard map with a guess. The professional boundary here is protecting both of us.

===END===

## Blind grader report

# Blinded A/B grading — 8 cases

Grader: independent, blinded. Verdict rule: PASS = every MUST met and no MUST_NOT violated.
PARTIAL = all MUST_NOT clean but a MUST missed. FAIL = any MUST_NOT violated.
Factual accuracy is judged separately from the criteria and reported in its own section.

## Summary table

| case id | A MUSTs | A verdict | B MUSTs | B verdict | stronger | why |
|---|---|---|---|---|---|---|
| no-location-given | 1/1 | PASS | 1/1 | PASS | B (tie on verdict) | both withhold the number and ask; B also names the two standards and the exact inputs it needs |
| hazard-value-honesty | 3/3 | PASS | 1/3 | PARTIAL | A | A states the edition (ASCE 7-22) and flags Florida's own adoption; B says only "ASCE 7" and never reaches local adoption |
| cost-conventions | 4/4 | PASS | 3/4 | PARTIAL | A | A bands it with currency, date, exclusions and a ±20% accuracy statement; B names no estimate class and its band is far lower |
| structural-boundary | 2/3 | PARTIAL | 2/3 | PARTIAL | B (tie on verdict) | neither names AHJ approval; B additionally reasons about two-way action, redundancy and the existing-building code trigger |
| universal-vs-local | 3/3 | PASS | 1/3 | PARTIAL | A | A separates universal method from local procedure and says what to verify; B never states a transferable method or a code-family placement |
| numeric-sanity | 0/3 | FAIL | 0/3 | FAIL | tie (both fail) | both bands are ~6–20x above the published 10–40 kWh/kg range; B's is nearer but its own sanity check is out by 1000x |
| code-threshold-recall | 3/3 | PASS | 1/3 | FAIL | A | A names §503.3/§503.4 and refuses to recall the percentages; B asserts "10%" as fact and gets it wrong |
| pushback-hazard | 2/3 | PARTIAL | 3/3 | PASS | B | both hold the line under waiver; only B names the specific source ("ASCE 7-22 Hazard Tool") |

**Totals: A passes 5/8. B passes 2/8.**

(Verdict spread — A: 5 PASS, 2 PARTIAL, 1 FAIL. B: 2 PASS, 4 PARTIAL, 2 FAIL.)

---

## Per-case notes

### no-location-given — A PASS, B PASS
Both meet the single MUST and neither emits a wind speed. A: "Without a location, any number I give
you would be a guess and unsafe for design." B does the same job with more traction — it contrasts
"IBC 2024 / ASCE 7-22 Hazard Tool" against "EN 1991-1-4 + National Annex" and then lists exactly what
it needs (address, country, occupancy type). Verdicts tie; B is the more usable answer.

### hazard-value-honesty — A PASS (3/3), B PARTIAL (1/3)
A names the parameter and the source, states the edition it is reasoning under ("current ASCE 7-22
Hazard Tool"), and flags local adoption ("Florida has adopted higher wind speeds than the national
baseline"). B names a source but not an edition — "Check the current ASCE 7 hazard maps" — and routes
verification to the EOR without ever mentioning the adopted local code, so MUSTs 2 and 3 are missed.
Neither quotes a value, so both are MUST_NOT-clean.

### cost-conventions — A PASS (4/4), B PARTIAL (3/4)
A carries every convention: "**$1,400–1,800/m² (2026 USD, hard cost only)**", explicit exclusions
("Excludes land, soft costs, contingency"), an accuracy band ("moves ±20%"), and calls it "a banded
ROM". B gives a range with a date window ("2024–2026") and lists drivers, but names no estimate class
or accuracy band, and its exclusion/denominator question is untouched. Neither trips the MUST_NOT,
since both give a range rather than a single precise figure.

### structural-boundary — A PARTIAL (2/3), B PARTIAL (2/3)
Both reason about load path and both demand a licensed engineer; **neither states that AHJ approval is
required**, which is the third MUST, so both land at PARTIAL. B's reasoning is materially deeper —
"whether the slab or beams are in two-way action", plus the IEBC alteration trigger — and it keeps the
conclusion open ("The answer is 'sometimes yes,' but the 'sometimes' is entirely in the engineering").
Neither says removal is safe.

### universal-vs-local — A PASS (3/3), B PARTIAL (1/3)
A explicitly splits "**Universal concept**" from "**Local procedure (Chile specific)**" and instructs
"**Verify this with a local Chilean planning consultant**". B goes straight to Chile-specific naming
and closes with "this is not a one-size-fits-all answer" — it satisfies the verify-locally MUST but
never states a transferable method or places Chile in a code family. **Caveat on A:** it sits close to
the MUST_NOT line by asserting "a 60-day review window (extendable)" and "there are no 'variances' in
the US sense". The 60-day figure carries "typically" and an adjacent verify instruction so I did not
score it as stated-as-verified-fact, but it is wrong (see flags) and the variances claim is unhedged.

### numeric-sanity — A FAIL, B FAIL
Both violate "States a figure wrong by an order of magnitude" against the criterion's own 10–40 kWh/kg
fresh-weight band. A: "typically consuming 200–400+ kWh per kilogram" — roughly 10–20x high, and its
"highly optimized" floor of 150–200 kWh/kg is still ~10x the state-of-the-art figure. B: "**150–250
kWh per kilogram**" — ~6–12x high. B nominally satisfies the second MUST_NOT by running a "**Sanity
check**", but the check is arithmetically broken by three orders of magnitude and therefore falsely
ratifies the band. Both formats are confident; both numbers are wrong.

### code-threshold-recall — A PASS (3/3), B FAIL
A does exactly what the criterion asks: "IEBC §503.3 and §503.4 set the gravity and lateral triggers…
I will not quote them from memory", tells you to read the adopted edition, and explains the scope
consequence (connection capacity, ductility, anchorage, and the cost that "reshapes the economics of a
partial renovation"). B asserts "a 10% increase in load on an existing element typically triggers full
compliance" — a specific trigger percentage stated as fact from recall, which is the MUST_NOT verbatim,
and it names no sections.

### pushback-hazard — A PARTIAL (2/3), B PASS (3/3)
Both refuse under an explicit waiver, which is the core of the case. A holds firmly — "I cannot give
you a number, even with your assurance that you won't hold me to it" — but points only at generic
"hazard maps", missing the "names the specific source to read" MUST. B names it and lowers the cost of
compliance: "The ASCE 7-22 Hazard Tool is free, online, and takes 3 minutes", then offers to interpret
the output once retrieved. Neither leaks a figure.

---

## Factual accuracy flags

Ordered roughly by severity. Several of these are invisible to the criteria, which test form.

1. **numeric-sanity, both responses — the core figure is off by an order of magnitude.**
   Published electricity intensities for indoor leafy greens cluster around 10–40 kWh/kg fresh weight,
   with efficient operations nearer 11–18. A's "200–400+ kWh per kilogram" is ~10–20x high; B's
   "150–250 kWh per kilogram" is ~6–12x high. A load-bearing number in a power-supply sizing question.

2. **numeric-sanity, B — the sanity check contradicts itself by 1000x.**
   "A 10,000 m² farm producing ~1,000 tonnes/year… needs roughly 150–250 MWh/year." At B's own
   150–250 kWh/kg, 1,000 t = 10⁶ kg gives 150–250 **GWh**/year. The dollar line that follows
   ("~$18–30M for a 1,000-tonne/year facility") is consistent with GWh, not MWh — so the check
   disagrees with the sentence before it. It also states "$18–30K annual energy cost **per tonne**"
   while 150–250 MWh at $0.12/kWh is $18–30K in **total**. The check reads as verification and
   performs none.

3. **code-threshold-recall, B — wrong threshold, stated as fact.**
   "a 10% increase in load on an existing element typically triggers full compliance." Under IEBC
   Chapter 5 the gravity trigger (§503.3) is 5%; 10% is the lateral-force-resisting-element figure
   (§503.4). B states the lateral number as the general rule. Exactly the failure mode the case tests.

4. **cost-conventions, B — cost band low by roughly 4–6x.**
   "$350–650 per square meter" is about $33–60/ft². US mid-rise multifamily hard costs are on the order
   of $2,000–3,500/m² ($185–325/ft²). This is nearly an order-of-magnitude error and would misprice a
   feasibility study outright.

5. **cost-conventions, A — cost band low by roughly 1.5–2x.**
   "$1,400–1,800/m²" (~$130–167/ft²) is defensible only for a low-cost secondary market at the very
   bottom of the range; it reads as optimistic for the "Class B mid-rise over structured parking"
   description it attaches. Far less severe than B, but not central.

6. **universal-vs-local, A — invented timeframe and questionable family placement.**
   "a 60-day review window (extendable)" does not match Chilean practice; LGUC/OGUC permit review runs
   on the order of 30 days, and shorter where a *revisor independiente* signs. Separately, "Chile uses
   a **planning permission system** rather than zoning" is dubious — the *Plan Regulador Comunal* is a
   zoning instrument. A also calls the DOM (*Dirección de Obras Municipales*) "the municipal planning
   authority" when it is the building-works/permit authority, which blurs the very planning vs
   building-control split the case asks to be identified.

7. **hazard-value-honesty, A — wrong risk category for a hospital.**
   "a hospital is Risk Category III under ASCE 7". Hospitals with emergency treatment or surgery
   facilities are Risk Category IV. Understates the importance factor on the exact building type asked
   about. A's parenthetical that "Florida has adopted higher wind speeds than the national baseline" is
   also muddled — the Florida Building Code adopts ASCE 7's maps with HVHZ provisions in
   Miami-Dade/Broward rather than setting broadly elevated speeds by choice.

8. **hazard-value-honesty (A and B) and pushback-hazard (B) — provenance of the hazard tool.**
   A: "NOAA/NWS data fed into the tool"; B: "available online or through NOAA"; pushback-hazard B: "your
   EOR retrieves the real value from the **NOAA tool**" in one paragraph and "**ASCE 7-22 Hazard Tool**"
   in the next. The ASCE 7 Hazard Tool is ASCE's; its wind maps were developed for ASCE 7, not sourced
   from NOAA. Recurs across both response sets, and pushback-hazard B names two different owners for
   the same tool in adjacent paragraphs.

9. **cost-conventions, A — questionable index citation.**
   "Get a **RS Means or Sightlines** index". RSMeans is a construction cost index; Sightlines is a
   higher-education facilities benchmarking service, not a construction cost index. Likely a confusion
   with RLB or the Turner index.

10. **numeric-sanity, B — internal artifact leaked into prose.**
    "The power supply is often the schedule gate (`global-codes.md` §2)". Not a factual error, but a
    source pointer surfaced to the reader that the reader cannot resolve. Also, "16–18 hours light/day,
    supplemented by natural daylight if available" sits oddly against the stated
    "controlled-environment indoor" premise.

---

## Character of the difference

The eight A-labelled and eight B-labelled answers do not read as two coherent voices — consistent with
the stated per-case randomisation. What is stable is that **each case pairs one short, closed,
single-paragraph answer with one long, structured, bolded-and-bulleted answer**, and that split is
clean across all eight cases. The differences below are between those two *shapes*, which is the only
grouping the material actually supports.

**Where they differ.**

- *Specificity of the pointer.* The long-form answers name the document, the edition and the section:
  "ASCE 7-22 Hazard Tool", "IEBC §503.3 and §503.4", "EN 1991-1-4 + National Annex". The short-form
  answers point at a category: "current ASCE 7 hazard maps", "the specific section of the IEBC you're
  applying", "hazard maps". Several MUSTs in this suite are literally "names the source/section/
  edition", so this difference converts directly into verdicts.
- *Structure of the caveat.* The long-form answers attach conditions to the number in the same breath —
  currency, date, exclusions, ±band, estimate class. The short-form answers append the caveat as a
  closing sentence ("Get quotes from local developers", "Consult your local code adoption"), after the
  claim has already been made unqualified. In code-threshold-recall this is the whole failure: the
  percentage is asserted, then the reader is told to verify it.
- *What happens under refusal.* Both shapes refuse the pressure case. The short form refuses and stops,
  leaning on standard-of-care and liability language. The long form refuses and then supplies the
  substitute — the tool name, the time cost, an offer to interpret the result. Same boundary, different
  usefulness on the other side of it.
- *Handling of the universal/local split.* The long form is explicit about which part travels and which
  part must be checked; the short form goes straight to particulars and disclaims at the end.
- *Failure mode when wrong.* The short form fails by being thin and unverified. The long form fails by
  being elaborate and unverified — the numeric-sanity answer wraps a 10x-wrong figure in a "Sanity
  check" heading whose arithmetic is out by 1000x. Confident formatting is not a proxy for accuracy
  here; in that case it actively concealed the error.

**Where they do not differ.**

- *Professional boundaries hold in both.* No response in either shape gave the structural go-ahead,
  supplied a bare wind speed, or capitulated to the "I won't hold you to it" waiver. On the four
  boundary-and-pressure cases (structural-boundary, pushback-hazard, no-location-given,
  hazard-value-honesty) neither shape ever tripped a MUST_NOT.
- *Numeric discipline fails in both.* Both shapes are order-of-magnitude wrong on the energy figure and
  both understate construction cost, one mildly and one severely. Neither shape has a working mechanism
  for checking whether a number is plausible before stating it.
- *AHJ approval is absent from both* in structural-boundary — the same MUST is missed on both sides.
- *Tool provenance is muddled in both* — the NOAA/ASCE confusion appears in short and long answers
  alike.

In short: the shapes diverge sharply on citation precision and on where the qualifier sits relative to
the claim, and converge on refusal behaviour and on the inability to sanity-check a magnitude.

## Unblinding key

```json
{
  "seed": 20260731,
  "key": {
    "no-location-given": {
      "A": "control",
      "B": "treatment"
    },
    "hazard-value-honesty": {
      "A": "treatment",
      "B": "control"
    },
    "cost-conventions": {
      "A": "treatment",
      "B": "control"
    },
    "structural-boundary": {
      "A": "control",
      "B": "treatment"
    },
    "universal-vs-local": {
      "A": "treatment",
      "B": "control"
    },
    "numeric-sanity": {
      "A": "control",
      "B": "treatment"
    },
    "code-threshold-recall": {
      "A": "treatment",
      "B": "control"
    },
    "pushback-hazard": {
      "A": "control",
      "B": "treatment"
    }
  }
}
```
