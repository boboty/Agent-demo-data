#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR/skills"
TARGET_DIR="$HOME/.agents/skills"
STAMP="$(date +%Y%m%d-%H%M%S)"
SKILLS=(
  amazon-review-insights
  amazon-return-reduction
  amazon-inventory-watch
  amazon-listing-localizer
  amazon-a-plus-planner
  supplier-quote-compare
  customer-service-triage
  business-file-organizer
)

echo "BrewGo Codex Skills installer"
echo "Target: $TARGET_DIR"

for skill in "${SKILLS[@]}"; do
  if [[ ! -f "$SOURCE_DIR/$skill/SKILL.md" ]]; then
    echo "ERROR: missing package file: skills/$skill/SKILL.md" >&2
    exit 1
  fi
done

conflicts=()
for skill in "${SKILLS[@]}"; do
  [[ -e "$TARGET_DIR/$skill" ]] && conflicts+=("$skill")
done

if (( ${#conflicts[@]} > 0 )); then
  echo "Existing skills with the same names:"
  printf '  - %s\n' "${conflicts[@]}"
  echo "If you continue, each existing directory will be backed up with suffix .backup-$STAMP."
  read -r -p "Continue? [y/N] " answer
  case "$answer" in
    y|Y|yes|YES) ;;
    *) echo "Installation cancelled; no existing skill was changed."; exit 1 ;;
  esac
fi

mkdir -p "$TARGET_DIR"
for skill in "${SKILLS[@]}"; do
  if [[ -e "$TARGET_DIR/$skill" ]]; then
    mv "$TARGET_DIR/$skill" "$TARGET_DIR/$skill.backup-$STAMP"
    echo "Backed up: $skill"
  fi
  cp -R "$SOURCE_DIR/$skill" "$TARGET_DIR/$skill"
done

echo
echo "Installed 8 BrewGo Skills:"
printf '  - %s\n' "${SKILLS[@]}"
echo
echo "Codex normally detects new skills automatically. If they do not appear in Skills or /skills, restart Codex."

