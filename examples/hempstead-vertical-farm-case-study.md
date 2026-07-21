# I Built an AI "Master Builder," Then Pointed It at My Own Grad-School Thesis

Ten years ago, a writing professor was unimpressed when I turned in a paper about growing food inside skyscrapers. I wrote at the time that he "was not a Master Builder." In 2021, that idea became my Georgetown capstone: a full development thesis and pro-forma model for converting a dead Home Depot and Modell's on Long Island into an indoor vertical farm. Twelve thousand words, real CoStar comps, a joint-venture waterfall, the works.

This month I did something I'd recommend to anyone who builds things: I built a tool designed to be smarter than me about my own field, and then I let it tear my old work apart.

## What the "Master Builder" skill is

The tool is a **Claude Skill** — a structured set of instructions and reference material that changes how the AI reasons about a domain. I called it **master-builder**, after the old idea of the *capomastro*: one mind that holds an entire project, from raw land through design, construction, handover, operations, and eventual sale — anywhere in the world.

It's built to do a few things a generic chatbot won't:

- **Ground every answer in a real place.** Codes and permits are local; physics and money are universal. The skill refuses to give a "generic building" answer — it asks *where*, then derives the code family, the loads, the utility path, and the market from there.
- **Follow the money as the spine.** Every design or construction decision is a cash-flow decision in disguise.
- **Encode real engineering doctrine.** I distilled the working conventions from the platforms I've built — source-of-truth data models, staged validation gates, hard rails on irreversible actions — into a "build doctrine" the AI applies to any system.
- **Audit a model honestly.** This is the capability that mattered most here: a forensic pro-forma review that treats a spreadsheet as an argument made in numbers and hunts for where the argument breaks.

Then I fed it my own thesis and asked a simple question: *does this actually pencil?*

## What it caught in my own work

Here's the uncomfortable, useful part. The skill was fair — it credited the market research and the completeness — and then it found things I'd rather it hadn't.

**The model contradicted itself.** My operating tab reported net operating income around $8 million a year. My reversion tab, doing the arithmetic correctly, said $3.4 million. One of them had accidentally *added* operating expenses to income instead of subtracting them. The narrative in my paper quoted the wrong one.

**A million dollars of soft costs quietly fell out of the budget.** My itemized soft-cost schedule totaled about $1.07 million — architect, engineers, consultants, the expeditor. Only $25,000 of it actually flowed into my Sources & Uses. The rest simply vanished between tabs.

**A third of the hard cost was buying almost no energy.** I'd budgeted $5.8 million for 1,161 vertical wind turbines — 33% of my hard costs — to generate about 2% of the project's on-site power. On a dollars-per-kilowatt-hour basis, the wind was roughly *38 times worse than the solar sitting next to it.* I had even written that it might be worth value-engineering out. The skill's response was blunt: then do it.

**I had modeled zero vacancy. Forever. For an asset class that didn't exist yet.** And depreciation — a non-cash item — was sitting inside my operating expenses, quietly dragging down NOI. The power numbers had unit errors of several orders of magnitude ("$203,000 per *day*" for one tenant's electricity).

None of this is a knock on 2021-me. This is what every first pro forma looks like. The point is that a disciplined second read catches it — and now I have one that never gets tired.

## The correction that made the deal *better* — and revealed the real risk

Here's the twist. When the skill rebuilt the model — wind removed, soft costs restored, vacancy set to a realistic 10%, the NOI computed correctly, transfer taxes normalized — the *building* got **cheaper and stronger**. Total development cost dropped from $39.4 million to about $30.1 million. Yield-on-cost rose to ~10% against a 6.14% exit cap — a healthy ~390-basis-point development spread. On paper, the real estate penciled better than my original.

So the critique didn't kill the deal. It moved the risk to where the risk actually lived: **not in the building, but in the business.**

Indoor farming lives and dies on the cost of electricity. Grow-lighting 200,000 square feet runs on the order of 20 million-plus kilowatt-hours a year — call it $2 million-plus in power that a *tenant* has to cover from thin-margin leafy greens. My whole rent roll assumed five solvent tenants who could do that, forever, with no vacancy.

Then the skill checked my assumption against reality. Every marquee operator I'd named as a target tenant in 2021 — AeroFarms, Bowery, Plenty, AppHarvest — has since gone through bankruptcy or shut down. Roughly fourteen indoor-farming companies filed for bankruptcy in 2025 alone. The recurring cause was exactly the line item my model fumbled: energy and capital costs that the produce price could never cover.

My thesis was a good real-estate argument wrapped around a business the market hadn't figured out how to make work. The skill let me see that clearly — four years too late to change my grade, but exactly on time as a lesson in how to underwrite.

## Why I'm open-sourcing it

Two principles I build everything around showed up here. The first: **honest status beats optimistic status.** A pro forma that oversells is defective, not polite — and the same is true of a trading model, a construction schedule, or a slide deck. The second: **validate demand before capital.** The survivors in vertical farming did the unglamorous thing — they signed buyers before they built, and right-sized their facilities. The failures built cathedrals and hoped.

The master-builder skill is now open-source under **[@ibuilder](https://github.com/ibuilder)**, MIT-licensed, with the Hempstead thesis included as a worked case study — my own numbers, corrections and all. If you're a developer, a contractor, or an investor, you can install it and point it at your own deals. It will be fair to you. It will also tell you the truth.

My old professor was right that I wasn't a Master Builder yet. The difference, a decade on, is that now I can build one — and then have the humility to let it grade my homework.

---

*The master-builder skill and the corrected Hempstead model are available at [github.com/ibuilder](https://github.com/ibuilder). Built with Claude.*
