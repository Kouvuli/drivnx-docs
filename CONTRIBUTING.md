# Working in the DrivnX workspace

This repo (`trisonlab/drivnx-docs`) is the workspace that holds the product docs and the AI skill setup. The two code
repos are cloned inside it and each has its own guide:

- [drivnx-web/CONTRIBUTING.md](drivnx-web/CONTRIBUTING.md): the Phase 1 app
- [drivnx-landing/CONTRIBUTING.md](drivnx-landing/CONTRIBUTING.md): the public website

## 1. Set up

```bash
git clone git@github.com:trisonlab/drivnx-docs.git DrivnX
cd DrivnX
git clone git@github.com:trisonlab/drivnx-web.git
git clone git@github.com:trisonlab/drivnx-landing.git
```

Keep this layout: the code repos link to `../docs/` and `../ai-skills/`. `.gitignore` keeps them out of this repo, so
each one has its own history, branches and pushes. Run git inside the folder you changed.

Also ignored, and local only: `autopilot/` (run logs) and `.claude/` (your Claude Code settings).

## 2. The docs

| File | What it is | How to change it |
|---|---|---|
| `docs/DrivnX_Phase1_Development_Direction.md` | The approved, canonical Phase 1 direction. Both code repos build from it | Agree the change with the team first; it changes what the code repos build. Then update their requirements so they follow it |
| `docs/DrivnX_Phase1_Development_Direction.pdf` | The same document, printable | Never edit it; re-render it from the Markdown (below) after every change |
| `docs/DrivnX_Phase1_Review_Notes.md` | Findings from reviewing the direction, each with how it was resolved | Add new findings here |
| `docs/design-mocks/` | Palette mocks behind the landing site's colours | Add new mocks; don't overwrite ones a revision points to |
| `docs/archive/` | Superseded material (the reviewed PDF, Velora Product Vision v2) | Read only: kept for history |

Re-render the PDF from `docs/`. You need the Python `markdown` package and Chromium:

```bash
cd docs
python3 build_pdf.py DrivnX_Phase1_Development_Direction.md p.html
chromium --headless --no-pdf-header-footer --print-to-pdf=DrivnX_Phase1_Development_Direction.pdf "file://$PWD/p.html" && rm p.html
```

Commit the Markdown and the PDF together. Pushes and pull requests go to `trisonlab/drivnx-docs`.

## 3. Plane

Work is tracked in [Plane](https://app.plane.so/drivnx/), project DRIVN: one module per Phase 1 milestone (M1 to M9)
plus Website, and one work item per feature, ticket and launch step. Labels say which repo owns the item
(`drivnx-web`, `drivnx-landing`). A drivnx-web ticket's ID is its Plane key (`DRIVN-31`); features and criteria keep
their CFX IDs. The repos stay the source of truth and Plane mirrors them; each repo's CONTRIBUTING.md says how.

To let Claude Code update Plane, add Plane's MCP server once (it signs in with OAuth in the browser):

```bash
claude mcp add --transport http --scope user plane https://mcp.plane.so/http/mcp
```

## 4. Using the AI skills

Skills are installed per code repo, not in this one. **Start your AI session inside the repo you're changing**
(`cd drivnx-web` or `cd drivnx-landing`, then `claude` or `codex`). Only then does the tool load that repo's
`CLAUDE.md` / `AGENTS.md`, skills and guard hooks. A session started here at the workspace root gets none of them.

How to use the skills day to day (`/next-step` to start, the flow, the guard hooks) is in each code repo's guide.

## 5. Managing the skill setup

`ai-skills/` holds the setup that all the code repos share:

| File | What |
|---|---|
| `ai-skills/baseline.txt` | Skills every repo gets on top of AI Skill OS's always-on core, one per line |
| `ai-skills/drivnx-skills.sh` | Sets up a new repo, or applies `baseline.txt` to every repo |

```bash
ai-skills/drivnx-skills.sh init drivnx-<name> <stack skills...>   # set up a new repo
ai-skills/drivnx-skills.sh sync                                     # after editing baseline.txt
```

Both need the `ai-skills` CLI from AI Skill OS, which isn't published yet: **ask Trison Labs if you need it.** Using
the skills in the code repos doesn't need it.

After `sync`, commit the changed `.ai/`, `.claude/`, `.agents/`, `CLAUDE.md` and `AGENTS.md` in each code repo. Then
update the stack skills table in the [README](README.md) if a repo's list changed.
