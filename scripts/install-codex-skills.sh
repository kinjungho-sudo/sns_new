#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target="${CODEX_HOME:-$HOME/.codex}/skills"

mkdir -p "$target"

for skill_dir in "$repo_root"/codex-skills/*; do
  [ -d "$skill_dir" ] || continue
  name="$(basename "$skill_dir")"
  rm -rf "$target/$name"
  cp -R "$skill_dir" "$target/$name"
  echo "installed $name -> $target/$name"
done
