# Working in the DrivnX workspace

This repo (`trisonlab/drivnx-docs`) holds the product docs and the AI skill setup. It sits in a `DrivnX/` workspace
folder next to the other repos, and each code repo has its own guide:

- [drivnx-web/CONTRIBUTING.md](../drivnx-web/CONTRIBUTING.md): the Phase 1 app
- [drivnx-landing/CONTRIBUTING.md](../drivnx-landing/CONTRIBUTING.md): the public website

## 1. Set up

Set up with [drivnx-cli](https://github.com/trisonlab/drivnx-cli): one command creates the workspace, clones the
repos, installs their dependencies and connects Claude Code to Plane and Pumble. Its README is the team guide.

```
DrivnX/                 a plain folder, not a repo
├── drivnx-cli/         trisonlab/drivnx-cli: the drivnx command and the team guide
├── drivnx-docs/        trisonlab/drivnx-docs (this repo): docs/ and ai-skills/
├── drivnx-web/         trisonlab/drivnx-web
└── drivnx-landing/     trisonlab/drivnx-landing
```

Keep the repos side by side: the code repos link to `../drivnx-docs/docs/` and `../drivnx-docs/ai-skills/`.
Each repo has its own history, branches and pushes, so run git inside the folder you changed.

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

`drivnx install` connects Claude Code to Plane. Sign in once: in Claude Code type `/mcp`, pick *plane*, then
*Authenticate*.

## 4. How the team works

Sprints, the Thursday and Saturday meetings, the Pumble channels, the automatic daily report and the rules for keys
are in the [drivnx-cli README](https://github.com/trisonlab/drivnx-cli#how-we-work).

## 5. Using the AI skills

Skills are installed per code repo, not in this one. **Start your AI session inside the repo you're changing**
(`cd DrivnX/drivnx-web` or `cd DrivnX/drivnx-landing`, then `claude` or `codex`). Only then does the tool load that
repo's `CLAUDE.md` / `AGENTS.md`, skills and guard hooks. A session started in `DrivnX/` or here gets none of them.

How to use the skills day to day (`/next-step` to start, the flow, the guard hooks) is in each code repo's guide.

## 6. Managing the skill setup

`ai-skills/` holds the setup that all the code repos share:

| File | What |
|---|---|
| `ai-skills/baseline.txt` | Skills every repo gets on top of AI Skill OS's always-on core, one per line |
| `ai-skills/drivnx-skills.sh` | Sets up a new repo, or applies `baseline.txt` to every repo |

Run them from the `DrivnX/` folder:

```bash
drivnx-docs/ai-skills/drivnx-skills.sh init drivnx-<name> <stack skills...>   # set up a new repo
drivnx-docs/ai-skills/drivnx-skills.sh sync                                     # after editing baseline.txt
```

Both need the `ai-skills` CLI from AI Skill OS, which isn't published yet: **ask Trison Labs if you need it.** Using
the skills in the code repos doesn't need it.

After `sync`, commit the changed `.ai/`, `.claude/`, `.agents/`, `CLAUDE.md` and `AGENTS.md` in each code repo. Then
update the stack skills table in the [README](README.md) if a repo's list changed.
