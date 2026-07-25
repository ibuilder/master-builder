# Master Builder — a Claude Skill for the built environment

[![CI](https://github.com/ibuilder/master-builder/actions/workflows/ci.yml/badge.svg)](https://github.com/ibuilder/master-builder/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Skill](https://img.shields.io/badge/type-Claude%20Skill-6366f1)
![Domain](https://img.shields.io/badge/domain-AEC%20%C2%B7%20real%20estate-33d17a)

> **Reason like a master builder** — one mind holding an entire built-asset project from raw land
> through design, construction, handover, operations, and disposition, **anywhere in the world.**

The historical *master builder* — the capomastro, the Baumeister, the architectus — was one person
who understood the whole: the ground, the money, the code, the crew, the materials, and the life of
the building after handover. This [Claude Skill](https://docs.claude.com) restores that unified mind.
Hand it any fragment of a project — a wind-load question, a line in a pro forma, a schedule slip — and
it reasons about that fragment inside the whole.

## What it does

- **Grounds every answer in a real place.** Codes and permits are local; physics and money are
  universal. It derives the governing code family, loads, utility path, and market from the site
  instead of giving a generic answer.
- **Follows the money as the spine.** Every design or construction decision is treated as the
  cash-flow decision it actually is.
- **Reviews models forensically.** Treats a pro forma as an argument made in numbers and audits it
  for integrity — the capability behind the [case study](#case-study) below.
- **Encodes real build doctrine.** Source-of-truth data models, staged validation gates, hard rails
  on irreversible actions, honest status over optimistic status, compliance-as-code.
- **Thinks globally.** A method for reasoning about unfamiliar jurisdictions by code family (ICC/IBC,
  Eurocodes, NCC, NBCC, IS/NBC India, GB China, Japan BSL, Middle East).
- **Counts the carbon, the climate risk, and the power.** Treats whole-life and embodied carbon as a
  cost and a risk (CBAM, Buy Clean, LEED v5, transition risk), climate resilience as adaptation the asset
  is underwritten against (flood/ASCE 24, stormwater, wildfire, heat), and the utility-interconnection
  queue as the schedule gate it has become for energy-intensive projects.
- **Allocates risk instead of naming it.** Who can control, price, *and* absorb each risk — through the
  contract clauses that actually fight, the right insurance product, a bond, or contingency — plus
  whether the project is *insurable* at all in a hardening climate market.
- **Works on buildings that already exist.** Conversion and retrofit on their own terms: the physical
  screen, the existing-building code path (IEBC), hazmat and structural due diligence,
  office-to-residential economics, and building-performance mandates like LL97 and EU MEPS.

## Install

A "skill" is just a folder — `SKILL.md` plus the `references/`. Pick the one path below that matches how
you use Claude. You only need to do this once.

### Option 1 — one command (Claude Code, or the Claude desktop app)

Paste this into your terminal. It drops the skill into your personal skills folder, which **both Claude
Code and the Claude desktop app read from** — so you install once and it works in both:

**macOS / Linux:**
```bash
git clone https://github.com/ibuilder/master-builder.git ~/.claude/skills/master-builder
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/ibuilder/master-builder.git "$env:USERPROFILE\.claude\skills\master-builder"
```

Then start (or restart) Claude and just ask a building question — it triggers on its own. In Claude Code
you can also type `/master-builder`, and `/skills` lists what's loaded. To update later, `pull` the folder:

```bash
git -C ~/.claude/skills/master-builder pull      # Windows: git -C "$env:USERPROFILE\.claude\skills\master-builder" pull
```

*No git?* [Download the ZIP](https://github.com/ibuilder/master-builder/archive/refs/heads/main.zip),
unzip it, and rename/move the folder so the path is `~/.claude/skills/master-builder/SKILL.md`.

### Option 2 — no terminal (Claude.ai in a browser, or the desktop app UI)

1. In Claude, open **Settings → Capabilities** and switch on **Code Execution** and **File Creation**
   (Skills need these turned on).
2. Download **[`master-builder.zip`](https://github.com/ibuilder/master-builder/releases/latest/download/master-builder.zip)**
   from the [latest release](https://github.com/ibuilder/master-builder/releases/latest).
3. Go to **Settings → Capabilities → Skills**, click **＋ → Upload skill**, and pick that `.zip`.
4. It shows up in your Skills list with an on/off toggle — switch it on. Done.

   *(The ZIP is already shaped the way the uploader wants — a `master-builder/` folder with `SKILL.md`
   inside — so it just works; no unzipping needed.)*

### By hand / other runtimes

Point your tooling at `SKILL.md` and the `references/` folder, or drop the folder at
`.claude/skills/master-builder/` inside a single project to scope it to that project.

## Use it in other assistants (ChatGPT, Gemini, Perplexity, or any model)

A Claude *skill* is a Claude-specific wrapper, but the knowledge inside it is plain, MIT-licensed
Markdown — so it works in **any** assistant. Grab the one-file bundle and paste it in:

**⬇ [`master-builder.bundle.md`](https://github.com/ibuilder/master-builder/releases/latest/download/master-builder.bundle.md)**
— the whole skill (the protocol + every reference) concatenated into a single file, with setup notes
at the top. (Also in the repo at [`dist/master-builder.bundle.md`](dist/master-builder.bundle.md).)

| Assistant | Setup |
|---|---|
| **ChatGPT** | New **Custom GPT** (or a Project) → paste the *Master Builder Protocol* section into **Instructions**, and upload `master-builder.bundle.md` (or the individual reference files) as **Knowledge**. |
| **Google Gemini** | New **Gem** → paste the bundle into the instructions, or attach it as a knowledge file. |
| **Perplexity** | New **Space** → paste the protocol into the Space's custom instructions and add the bundle (or this repo's link) as a source. |
| **Any API / open model** | Prepend `master-builder.bundle.md` to your system prompt. |

**Trade-off:** the bundle loads everything at once, so you lose Claude's load-on-demand *progressive
disclosure* (reading only the reference a task needs). That's fine for large-context models — just
heavier on tokens. If your tool speaks MCP, the server below gives you that back.

## Use it as an MCP server (any MCP-capable agent)

For agents that speak the [Model Context Protocol](https://modelcontextprotocol.io), the repo ships a
server that hands out the protocol and references **on demand** — so the agent pulls only the reference
a task needs instead of loading the whole corpus. That restores progressive disclosure outside Claude.

It is **stdlib-only Python 3.9+** — nothing to `pip install`, no SDK to pin, runs offline. Point your
client at it:

```json
{
  "mcpServers": {
    "master-builder": {
      "command": "python",
      "args": ["/absolute/path/to/master-builder/scripts/mcp_server.py"]
    }
  }
}
```

Four read-only tools: `master_builder_get_protocol`, `master_builder_list_references`,
`master_builder_read_reference`, `master_builder_search` (plus the same corpus as MCP *resources*).
Verify it any time with:

```bash
python scripts/mcp_server.py --selftest
```

## Structure

```
SKILL.md                         # the Master Builder Protocol + ground-in-place rule + boundaries
references/
  global-codes.md                # jurisdictions, code families, load derivation, the AHJ, utility gates
  development-lifecycle.md        # origination → feasibility → entitlements → design gates → ops → exit
  real-estate-finance.md         # pro formas, returns, capital stack, construction loans, JV waterfalls
  construction-delivery.md        # delivery methods, contracts (AIA/FIDIC/NEC/JCT), estimating, scheduling
  risk-insurance.md              # risk allocation, contract clauses, insurance, surety, insurability, contingency
  adaptive-reuse.md              # existing buildings — conversion, IEBC code paths, hazmat DD, retrofit mandates
  digital-toolkit.md             # BIM/IFC, ISO 19650/CDE, 4D/5D, reality capture, the software map
  sustainability-carbon.md       # whole-life & embodied carbon, LCA/EPDs, CBAM/Buy Clean, transition risk, resilience
  build-doctrine.md              # cross-cutting engineering lessons for building any system
  pro-forma-review.md            # forensic model/deal audit — reframe, reconcile, defect checklist
examples/
  hempstead-vertical-farm-case-study.md   # using the skill to critique the author's own 2021 thesis
  hempstead-corrected-model.xlsx          # the rebuilt, formula-driven feasibility model
scripts/
  build.py                       # regenerates every dist/ artifact from the source (one build command)
  mcp_server.py                  # zero-dependency MCP server (stdio) — serves the skill on demand
  validate.py                    # enforces the authoring rules (lean SKILL.md, table ↔ files, links)
dist/                            # generated — do not edit by hand
  master-builder.skill           # installable Claude skill (zip)
  master-builder.zip             # same package, .zip extension for the claude.ai uploader
  master-builder.bundle.md       # one-file portable bundle for any other assistant
```

Everything in `dist/` is generated from `SKILL.md` + `references/` by **`python scripts/build.py`** — so
the packages and the bundle can never drift from the source. Progressive disclosure: `SKILL.md` stays
lean (~170 lines) and carries a table pointing to the ten reference files, which load only when the
task needs them.

## Case study

[`examples/hempstead-vertical-farm-case-study.md`](examples/hempstead-vertical-farm-case-study.md) —
the author pointed the skill at his own 2021 Georgetown capstone (converting a dead big-box into an
indoor vertical farm) and let it audit the pro forma. It caught a self-contradicting NOI, ~$1M of
soft costs dropped between tabs, a wind array that was 33% of hard cost for ~2% of the energy, and a
zero-vacancy assumption for an asset class that has since seen ~14 bankruptcies. The corrected,
formula-driven model is included. The building deal got *stronger*; the risk turned out to live in the
business, not the real estate.

## Provenance

Built from 22+ years of construction and real-estate development practice and the working conventions
of open platforms in this org (notably [Massing](https://github.com/ibuilder/massing) — an IFC-native
AEC platform). Standards references were verified against current editions as of **July 2026**: IBC 2024
/ ASCE 7-22 (ICC 2027 in development), second-generation Eurocodes (publish 2027 / withdraw 2028),
NCC 2025, ISO 19650 second-generation DIS (Mar 2026) + IFC/ISO 16739-1:2024, LEED v5, RICS WLCA 2nd ed
+ EN 15978, and the EU CBAM definitive period (live Jan 2026).

## Contributing

Issues and PRs welcome — especially country/jurisdiction dossiers, additional worked case studies, and
corrections to code-edition references. Keep `SKILL.md` lean; put depth in `references/`.

## License

[MIT](LICENSE) © Matthew M. Emma / ibuilder. Built with Claude.
