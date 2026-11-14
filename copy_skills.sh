#!/usr/bin/env bash
# Copy all unique skill directories into this repo under ./skills/ preserving hierarchy.
set -euo pipefail

SRC_ROOT="/home/rpulido/Documents/repos"
DEST_ROOT="$(pwd)/skills"

# Find all SKILL.md files, excluding duplicates in .codex-marketplace and .github/.agents
find "$SRC_ROOT" -type f -name "SKILL.md" \
  | grep -vE "\.codex-marketplace|\.github|\.agents|\.venv|\.git" \
  | while read -r skill_file; do
    skill_dir=$(dirname "$skill_file")
    # Compute relative path from SRC_ROOT
    rel_path=${skill_dir#${SRC_ROOT}/}
    # Destination path under skills/<rel_path>
    dest_path="$DEST_ROOT/$rel_path"
    # Ensure destination parent exists
    mkdir -p "$(dirname "$dest_path")"
    # Copy the whole skill directory (including references, assets, etc.)
    cp -a "$skill_dir" "$dest_path"
    echo "Copied $rel_path"
  done
