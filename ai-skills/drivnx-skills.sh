#!/usr/bin/env bash
# AI Skill OS setup shared by every DrivnX repo (repos live directly in this workspace folder).
#   drivnx-skills.sh init <repo-dir> [stack-skill ...]   set up a new repo: baseline.txt + its own stack skills
#   drivnx-skills.sh sync                                add baseline.txt to every repo that is already set up
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
workspace="$(dirname "$here")"
mapfile -t baseline < <(sed 's/#.*//; s/[[:space:]]//g; /^$/d' "$here/baseline.txt")

case "${1:-}" in
  init)
    repo="${2:?usage: drivnx-skills.sh init <repo-dir> [stack-skill ...]}"
    includes=()
    for skill in "${baseline[@]}" "${@:3}"; do includes+=(--include "$skill"); done
    # Resolved relative to the repo, so it holds for any repo directly under the workspace.
    ai-skills init "$repo" --portable --adapter agents,claude \
      --requirements ../docs/DrivnX_Phase1_Development_Direction.md "${includes[@]}" -y
    ;;
  sync)
    for manifest in "$workspace"/*/.ai/manifest.yaml; do
      ai-skills add --project "${manifest%/.ai/manifest.yaml}" "${baseline[@]}"
    done
    ;;
  *) sed -n '2,4p' "$0"; exit 2 ;;
esac
