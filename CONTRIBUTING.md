# Contributing to Master Builder

Thanks for helping build this out.

## Principles
- **Keep `SKILL.md` lean.** It should stay well under ~500 lines and route to `references/`.
- **Depth goes in `references/`.** One file per domain; add a new file rather than bloating an existing one.
- **Ground claims.** Cite the current code edition or standard; note when a value must be locally verified.
- **Universal vs local.** Separate transferable reasoning from jurisdiction-specific values.

## Especially welcome
- Country / jurisdiction dossiers (code family, AHJ, load basis, licensure).
- Additional worked case studies under `examples/`.
- Corrections to code-edition or standard references as cycles update.

## Workflow
1. Fork and branch.
2. Make the change; if it touches triggering, update the `description` in `SKILL.md` frontmatter.
3. Rerun the build so the packages and the portable bundle stay in sync with the source:
   ```bash
   python scripts/build.py
   ```
   Everything in `dist/` **and `plugin/skills/master-builder/`** is generated — never edit those by hand.
   If you add or rename a reference, the build picks it up automatically; just commit the result.
4. Check your work (CI runs exactly these, on Python 3.9 and 3.12):
   ```bash
   python scripts/validate.py            # structure, links, and the plugin manifests
   python scripts/eval_retrieval.py      # every question still routes to the right reference
   python scripts/eval_behavior.py --check
   python scripts/mcp_server.py --selftest
   ```
   If you add substantial new material, add a retrieval case for it in `evals/retrieval.jsonl` — a
   topic the eval doesn't cover can silently rot.
5. Open a PR describing what changed and why.

All three scripts are **stdlib-only** — no dependencies, no lockfile, nothing to install. Keep it that way.
