#!/usr/bin/env bash
set -euo pipefail

ROOT="$(pwd)"
OUT="$ROOT/INDEX.md"

echo "# Skill Index" > "$OUT"

echo "" >> "$OUT"

echo "| Skill Path | Title |" >> "$OUT"

echo "|---|---|" >> "$OUT"

find "$ROOT/skills" -type f -name "SKILL.md" | while read -r file; do
  # Get relative path
  rel=${file#${ROOT}/}
  # Extract first markdown heading (remove leading # and spaces)
  title=$(grep -m1 "^#" "$file" | sed 's/^#\s*//')
  # If title is empty, fallback to directory name
  if [ -z "$title" ]; then
    title=$(basename "$(dirname "$file")")
  fi
  echo "| $rel | $title |" >> "$OUT"
done
