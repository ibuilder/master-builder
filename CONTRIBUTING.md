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
   Everything in `dist/` is generated — never edit those files by hand.
4. Open a PR describing what changed and why.
