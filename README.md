# DrivnX workspace

DrivnX is the product and the company; Trison Labs is the team building it. Phase 1 lets a user connect unfamiliar data and turn it into evidence-backed, human-reviewed understanding and explicit data definitions.

**Source of truth:** [docs/DrivnX_Phase1_Development_Direction.md](docs/DrivnX_Phase1_Development_Direction.md), approved and canonical since 2026-10-30.

**New here?** Read [CONTRIBUTING.md](CONTRIBUTING.md) to set up the workspace, then each code repo's own `CONTRIBUTING.md` for its workflow and AI skills.

This repo sits in a `DrivnX/` workspace folder next to the other repos:

| Repo | What |
|---|---|
| [`drivnx-cli`](https://github.com/trisonlab/drivnx-cli) | The `drivnx` command that sets up the workspace, and the team guide |
| `drivnx-docs` (this one) | Product docs and the shared AI skill setup |
| [`drivnx-web`](https://github.com/trisonlab/drivnx-web) | The Phase 1 app (local FastAPI runtime + React browser UI) |
| [`drivnx-landing`](https://github.com/trisonlab/drivnx-landing) | Public website. Copy follows the Phase 1 direction since requirements revision 12 |

| Folder | What |
|---|---|
| `docs/` | Phase 1 direction (Markdown + PDF, figures; `build_pdf.py` re-renders the PDF), review notes, `design-mocks/` (the shipped orange palette), `archive/` (reviewed PDF, Velora Product Vision v2, its source image notes) |
| `ai-skills/` | AI Skill OS setup shared by every repo |

## AI skills for every repo

Every repo gets AI Skill OS's always-on core, plus the shared [ai-skills/baseline.txt](ai-skills/baseline.txt), plus its own stack skills:

```bash
# from the DrivnX/ workspace folder
drivnx-docs/ai-skills/drivnx-skills.sh init drivnx-<name> <stack skills...>   # new repo
drivnx-docs/ai-skills/drivnx-skills.sh sync                                     # after editing baseline.txt
```

| Repo | Stack skills on top of the baseline |
|---|---|
| drivnx-web | python api database-engineer postgres docker react frontend-design web-design-guidelines accessibility frontend-testing |
| drivnx-landing | nextjs react frontend-design web-design-guidelines accessibility frontend-testing web-motion-3d |
