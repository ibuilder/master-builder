# Climate & Building Science — the other half of the book

Two inputs generate most of what governs a building: **the municipal code** (what you're allowed to do,
and who approves it — `global-codes.md`) and **the climate** (what physics will do to the building for
the next fifty years). This file is the climate half.

Read it whenever the task touches envelope, assemblies, moisture, insulation, HVAC strategy,
foundations, durability, or "how should this be built *here*."

The reason this reference exists: **codes are local and change every three years; building physics is
universal and never changes.** A vapour barrier on the wrong side of a wall fails in Manitoba and in
Malaysia for exactly the same reason, and no code edition will save it. Get the physics right first,
then satisfy the local code — not the reverse.

## Contents
1. The one rule: heat and vapour move the same direction, and the control layers follow
2. The four control layers, in order
3. Air leakage beats diffusion — the correction most designers still need
4. Climate families and what each does to a building
5. Mixed climates — the genuinely hard case
6. Below grade and the ground
7. Durability: what the climate eats
8. Climate and the schedule
9. Universal vs local

---

## 1. The one rule: heat and vapour move the same direction, and the control layers follow

Water vapour moves from **warm and humid** toward **cool and dry**. That single sentence sets envelope
design everywhere on Earth:

- **Heating-dominated (cold) climate** — the interior is warm and moist most of the year, so the drive is
  **outward**. The vapour retarder belongs toward the **interior** (the warm side), and the assembly must
  be able to dry **outward**.
- **Cooling-dominated (hot-humid) climate** — the air-conditioned interior is the cool, dry side, so the
  drive is **inward**. Vapour control belongs toward the **exterior**, and the assembly must be able to
  dry **inward** — which means permeable interior finishes. Vinyl wallpaper on the inside face of an
  air-conditioned wall in the tropics is a mould factory.
- **Hot-dry climate** — vapour is a minor problem; heat gain, solar radiation, and thermal mass dominate.

> **Never trap an assembly between two impermeable layers.** The classic destroyed wall has a sealed
> membrane outside and a polyethylene sheet inside: whatever water gets in — and water always gets in —
> can dry in neither direction. **Every assembly must be able to dry in at least one direction.** If you
> take one thing from this file, take that.

The practical inversion to remember: **the correct detail in Minneapolis is the wrong detail in Miami,**
and it is the *same* physics producing both answers.

---

## 2. The four control layers, in order

Every enclosure — anywhere, any material, any budget — is managing four things. Design them explicitly,
name which material does each job, and detail the *transitions and penetrations*, because that is where
enclosures actually fail.

1. **Water (bulk rain)** — the most important and most commonly botched. Shed it: overhangs, flashings,
   sloped surfaces, and a continuous **drainage plane** behind the cladding. On exposed or
   wind-driven-rain sites, a **rain screen** (a vented, drained cavity that also relieves air-pressure
   difference) is the durable answer.
2. **Air** — the **air barrier**, continuous around the whole enclosure. This is the highest-leverage
   layer (see §3) and governs energy, comfort, moisture, and often sound.
3. **Vapour** — the vapour retarder, on the side §1 dictates. Often the same material as the air barrier;
   often *not*, and conflating the two causes real failures.
4. **Thermal** — insulation, ideally **continuous on the exterior** where it keeps the structure warm and
   above the dew point, and eliminates **thermal bridging** (studs, slab edges, balconies, and shelf
   angles quietly destroy nominal R-values).

Ordering rule: **control layers must be continuous and must connect to each other.** Draw a line for each
layer around the whole section without lifting the pen — wall to roof, wall to window, wall to slab. If
the line breaks, that break is the future failure and probably the future claim (`risk-insurance.md`).

---

## 3. Air leakage beats diffusion — the correction most designers still need

The profession spent decades arguing about vapour barriers while the actual moisture was riding air.
**Air leakage (advection) transports far more moisture into assemblies than vapour diffusion does** —
typically by orders of magnitude. Moist air pushed through a gap by wind, stack effect, or fan pressure
condenses on the first cold surface it finds.

Consequences worth acting on:

- **Prioritize air-tightness over vapour-barrier fixation.** A continuous, well-detailed air barrier does
  more good than a perfect vapour retarder with holes around every penetration.
- **The leaks that matter are penetrations and junctions** — window and door perimeters, roof fasteners,
  conduits, sprinkler heads, ductwork, light fixtures, slab-to-wall junctions.
- **Pressure matters.** In hot-humid climates, keeping the building slightly **positively** pressurized
  keeps humid outdoor air out of the walls; getting this backwards drives moisture *into* the enclosure.
  In cold climates the stack effect pushes moist indoor air up and out through the top of the building.
- **Tighter buildings need deliberate ventilation.** Air-tightness without designed mechanical
  ventilation trades a moisture problem for an indoor-air-quality problem.

---

## 4. Climate families and what each does to a building

Use **Köppen–Geiger** as the global spine — unlike national energy-code zone maps, it exists for every
point on Earth, so it works when you land somewhere with no familiar zoning system. Cross-map to the
local code's zones (ASHRAE 1–8, NCC 1–8, EU degree-days) when you need compliance numbers.

| Köppen family | Dominant problem | What it forces |
|---|---|---|
| **A — Tropical** (Af/Am/Aw) | Heat + relentless humidity; intense rain; termites; typhoons in belts | Vapour control **outside**, dry inward, permeable interior finishes; deep overhangs and rain screens; elevated/ventilated ground floors; mould and termite defence; dehumidification as a first-class load; cross-ventilation and shading before mechanical cooling |
| **B — Arid / semi-arid** (BWh/BSk) | Extreme heat, huge day–night swing, dust, scarce water; expansive/saline soils | **Thermal mass** + night flush; shading and small, protected glazing; light/reflective surfaces; evaporative cooling where humidity allows; dust-tolerant filtration; water reuse; sabkha/salt-attack protection of concrete |
| **C — Temperate** (Cfa/Cfb/Csa) | Both heating *and* cooling seasons; humid summers or wet winters | The hard case — assemblies must dry **both** ways (§5); shading for summer, insulation for winter; wet-winter Mediterranean/maritime zones punish poor rain control |
| **D — Continental** (Dfa/Dfb/Dfc) | Deep cold, long heating season, snow, freeze–thaw | Vapour retarder **inside**, dry outward; continuous exterior insulation; frost-depth foundations; snow loads and drift; ice damming and vented/warm-roof strategy; freeze–thaw-durable materials |
| **E — Polar / alpine** (ET/EF) | Extreme cold, permafrost, short build season | Elevated foundations preserving permafrost; extreme air-tightness; heat-recovery ventilation; logistics and a very short construction window dominate cost |

Two overlays cut across all of the above and often matter more than the family:
- **Marine/coastal** — salt-laden air drives **corrosion** (reinforcement, fixings, cladding, plant) and
  wind-driven rain; specify stainless/hot-dip fixings and cover to reinforcement accordingly.
- **Altitude** — thinner air reduces convective cooling and changes combustion, HVAC sizing, and UV exposure.

---

## 5. Mixed climates — the genuinely hard case

Where a building both heats and cools substantially (much of Köppen **C**, and US zones 3–5), **the
vapour drive reverses seasonally.** There is no single "correct side" for a vapour retarder, and the
naïve cold-climate detail — polyethylene on the interior — traps summer inward drive against it.

The strategy that works: **choose vapour-open assemblies that can dry in both directions**, use a
*vapour-semi-permeable* retarder rather than a vapour barrier, put insulation **outside** the structure to
keep the condensing surface warm, and get the air barrier genuinely continuous. Where the assembly is
unusual or the stakes are high, run a **hygrothermal (transient moisture) simulation** rather than
reasoning from rules of thumb — this is one of the few places where the modelling earns its fee.

> Codes encode this crudely. Many prescriptive rules require interior vapour retarders in colder zones
> and require none in hot zones — but a prescriptive pass is not proof the assembly dries. **A code-
> compliant wall can still rot.** Say so, and design the drying path deliberately.

---

## 6. Below grade and the ground

Climate reaches the building through the soil as much as through the air:

- **Frost depth** sets footing depth in freezing climates; get it wrong and the building heaves.
- **Expansive clays** (common in arid and semi-arid regions) swell and shrink with moisture — a leading
  cause of structural distress worldwide. They demand deepened/stiffened foundations, moisture
  stabilization, and disciplined site drainage.
- **Permafrost** must be kept frozen — elevated or thermally isolated foundations, or the building melts
  its own support.
- **Water table and hydrostatic pressure** decide whether below-grade space is a waterproofing problem or
  a drainage problem — and the two get different (and non-interchangeable) solutions.
- **Radon** and soil gas in some geologies; sub-slab depressurization is cheap at construction and
  expensive later.
- **Slab edges and grade beams** are the most common thermal bridge and the most common water entry —
  detail them together.

---

## 7. Durability: what the climate eats

Whole-life cost is decided by which of these the site will do to the building (`sustainability-carbon.md`):

- **Corrosion** — marine salt and de-icing salts attack reinforcement, fixings, and plant. Set concrete
  cover, admixtures, and metal grades to the exposure class, not to habit.
- **Freeze–thaw** — saturated porous materials spall; needs air-entrained concrete and correctly rated
  masonry, plus detailing that keeps water out in the first place.
- **UV and heat** — degrades sealants, membranes, and polymers fastest in high-insolation climates;
  drives real replacement cycles in the maintenance plan.
- **Biological** — termites (a design constraint across much of the tropics and subtropics, dictating
  barriers, treated timber, or non-timber structure), mould, and rot.
- **Wind-driven rain and abrasion** — dust and sand in arid regions abrade finishes and foul equipment.

Durability is a **design** decision, not a maintenance one. The building will get the climate it is in;
the only variable is whether the assemblies were chosen for it.

---

## 8. Climate and the schedule

Climate is also a programme and money question (`construction-delivery.md`, `real-estate-finance.md`):

- **The build window.** Deep-winter and monsoon regions have months where concrete, earthworks, or roofing
  simply cannot proceed to spec. A schedule that ignores the season is fiction, and the carry is real.
- **Temperature limits on the work itself** — hot- and cold-weather concreting have real rules
  (curing, protection, admixtures); mortar, sealants, membranes, and paints all have application windows.
- **Weather-sensitive activities and float** — sequence enclosure to get the building weather-tight before
  the bad season, and track weather-delay days against the contract's excusable-delay provisions
  (`risk-insurance.md` §3).
- **Design to the future climate, not the historical one** — cooling loads, storm intensity, and heat
  extremes are moving within the asset's life (`sustainability-carbon.md` §7).

---

## 9. Universal vs local

**Universal (travels everywhere):** vapour drives from warm-humid to cool-dry; every assembly must dry in
at least one direction; air leakage carries more moisture than diffusion; control layers must be
continuous and connected; thermal bridges destroy nominal performance; the ground and the sea attack
materials in predictable ways. None of this changes with jurisdiction.

**Local (must be verified):** the climate zone designation the code uses and its prescriptive
requirements, required R/U-values and vapour-retarder classes, frost depth, design temperatures and
humidity, rainfall intensity, ground snow, wind and seismic parameters, soil type and water table, and
termite/radon/salt exposure mapping. Read these from the local code and hazard maps — never from memory
(`global-codes.md` §4, and the worked examples in `jurisdiction-dossiers.md`).
