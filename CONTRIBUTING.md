# Working in the DrivnX workspace

This repo (`trisonlab/drivnx-docs`) holds the product docs, the AI skill setup and the team tools. It sits in a
`DrivnX/` workspace folder next to the two code repos, and each of those has its own guide:

- [drivnx-web/CONTRIBUTING.md](../drivnx-web/CONTRIBUTING.md): the Phase 1 app
- [drivnx-landing/CONTRIBUTING.md](../drivnx-landing/CONTRIBUTING.md): the public website

## 1. Set up

```
DrivnX/                 a plain folder, not a repo
├── drivnx-docs/        trisonlab/drivnx-docs: docs/, ai-skills/, bin/drivnx, team-tools/
├── drivnx-web/         trisonlab/drivnx-web
└── drivnx-landing/     trisonlab/drivnx-landing
```

You need git, Python 3.10+ and [Claude Code](https://claude.com/claude-code); the [GitHub CLI](https://cli.github.com)
(`gh auth login`) is recommended. Then:

```bash
mkdir DrivnX && cd DrivnX
git clone https://github.com/trisonlab/drivnx-docs.git
python3 drivnx-docs/bin/drivnx install        # Windows: py drivnx-docs\bin\drivnx install
```

`drivnx install` clones drivnx-web and drivnx-landing next to drivnx-docs and installs their dependencies from the
lockfiles. It also adds the Plane and Pumble MCP servers to Claude Code, asking for the Pumble keys (section 4). Then
it installs the team notifier and its daily-report job (cron, or Task Scheduler on Windows) and puts a `drivnx`
command on your PATH. It's safe to run again; it only fixes what's missing. Afterwards:

| Command | What it does |
|---|---|
| `drivnx status` | Health check: each repo's branch and changes, tools, MCP servers, hooks, daily job, AI skills. `--online` also tests the MCP connections |
| `drivnx update` | Pulls all three repos (fast-forward only; skips any with uncommitted changes) and refreshes the notifier |
| `drivnx report` | Previews today's daily report; `--post` posts it |
| `drivnx skills sync` | Applies `ai-skills/baseline.txt` to every code repo (section 6) |

Keep the three repos side by side: the code repos link to `../drivnx-docs/docs/` and `../drivnx-docs/ai-skills/`.
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

To let Claude Code update Plane, add Plane's MCP server once (it signs in with OAuth in the browser):

```bash
claude mcp add --transport http --scope user plane https://mcp.plane.so/http/mcp
```

## 4. Team tools: sprints, Pumble and Claude Code

### How we work

| When | What | Where |
|---|---|---|
| Sunday to Saturday | One sprint = one Plane cycle in DRIVN | Plane |
| Every day | Nothing to write: Claude Code posts your work and GitHub posts your PRs | Pumble |
| Thursday | Mid-sprint check-in: blockers, open PRs, re-plan if needed | Google Meet |
| Saturday | Sprint review, retro, and plan the next sprint | Google Meet |

Before each meeting, ask Claude Code to *"post the Thursday check-in"* or *"post the Saturday review"*. It reads
Plane and GitHub and posts a summary to `#meetings`. After Saturday's meeting, close the cycle in Plane and open the
next one.

### Pumble channels

| Channel | What lands there | Sent by |
|---|---|---|
| `#meetings` | Thursday check-in, Saturday review / retro / plan | Claude Code (when you ask) |
| `#daily-report` | Each person's day: commits, PRs, Claude tasks, skills used. Posted at 23:00 Vietnam time | Automatic |
| `#dev-activity` | "Claude finished" after each Claude Code task that changed files or made commits | Automatic |
| `#pr-web`, `#pr-landing`, `#pr-docs` | PR opened / reviewed / merged, pushes, issues, releases for that repo | Pumble GitHub app |
| `#general` | Everything else | You |

### Set up (once)

1. **Join Pumble:** accept the invite to the TrisonLab workspace (web app at [app.pumble.com](https://app.pumble.com),
   or the desktop and mobile apps).
2. **Get the two Pumble keys** from the workspace owner, in a Pumble direct message: the **App key** (`xpat-…`) and
   the **bot token** of the *Claude* app.
3. **Run `drivnx install`** in a normal terminal, not inside a Claude session, so the keys never reach a transcript.
   It asks for the two keys with hidden input. Then delete the direct message.
4. **Sign in to Plane:** in Claude Code, type `/mcp`, pick *plane*, then *Authenticate*.
5. **Restart Claude Code** and check with `drivnx status --online`. The next commit Claude makes posts a "Claude
   finished" message with your name to `#dev-activity`.

### Day to day

1. Pick a work item from the current cycle in Plane, assign it to yourself and move it to *In Progress*.
2. Branch as `feat/<plane-key>-short-name` (e.g. `feat/drivn-31-login-form`).
3. Open the PR with the Plane key at the start of the title (`DRIVN-31: Add the login form`). The repo's PR channel
   gets it.
4. After review, squash-merge. Move the item to *Done*.

Things you can ask Claude Code (it has the Plane and Pumble MCP servers):

- *"Move DRIVN-31 to Done and say so in #meetings"*
- *"What's still open in this sprint?"*
- *"Post the Thursday check-in"* / *"Post the Saturday review"*

Preview tonight's daily report without posting it: `drivnx report`. Its name and time come from
`~/.config/drivnx/pumble.json`.

### Rules

- **Keys never go in a repo or a chat.** Don't paste them into Pumble channels or into Claude: transcripts are stored
  on disk. If one leaks, tell the owner, who regenerates it.
- **The free Pumble plan allows 3 apps**: GitHub, Google Calendar and Claude. Agree with the team before adding one.
- **Group calls aren't free on Pumble**: meetings are on Google Meet.
- **New repo:** create its PR channel and run `/github subscribe trisonlab/<repo>` there *before* its first PR.
  Events from before the subscription are never posted.

### If something doesn't work

| Problem | Fix |
|---|---|
| Claude has no `send_message` tool for Pumble | The app is missing scopes: the owner adds them (below) and reinstalls it. Then run `claude mcp remove pumble -s user` and `drivnx install` with the new token |
| `drivnx status` shows a ✘ | Run `drivnx install` again; it fixes what's missing and leaves the rest |
| Nothing in `#dev-activity` or `#daily-report` | Read `~/.claude/hooks/pumble-notify.log`. "channel not found" means the Claude bot isn't in that channel: add it |
| A PR event is missing | The channel isn't subscribed to that repo, or it's a comment: comments aren't part of the subscription |

### Owner only: the Pumble app setup

- **Claude app** (Workspace settings → Configure apps). User *and* bot scopes: `messages:read`, `messages:write`,
  `files:write`, `messages:edit`, `messages:delete`, `channels:read`, `channels:list`, `channels:write`,
  `users:list`, `user:read`, `workspace:read`, `reaction:read`, `reaction:write`. Without `files:write` and
  `channels:list`, the MCP has no send or channel-list tools. The bot must be a member of `#meetings`,
  `#daily-report` and `#dev-activity`.
- **GitHub app**: on GitHub, trisonlab → Settings → GitHub Apps → *pumble-github* → give it access to each repo,
  then `/github subscribe trisonlab/<repo>` in that repo's PR channel.
- **Google Calendar app**: reminders for the Thursday and Saturday meetings go to `#meetings`.

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
