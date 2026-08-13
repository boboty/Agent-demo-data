#!/usr/bin/env python3
"""Safely remove only the Demo 05 BrewGo Search Term Skill from known locations.

The classroom skill is created live by Codex and should normally live inside the
workspace at workspaces/codex/05-search-term-skill/.agents/skills/ (so a normal
workspace rebuild clears it). If Codex instead wrote the skill to a user-global
skill directory, this script removes only that specific skill folder and nothing
else. It never deletes a parent skills directory or any other skill.
"""
from __future__ import annotations

import os
import shutil
from pathlib import Path

SKILL_NAME = "brewgo-search-term-analysis"
SOURCE_ROOT = Path(__file__).resolve().parents[1]

WORKSPACE_SKILL = SOURCE_ROOT / "workspaces" / "codex" / "05-search-term-skill" / ".agents" / "skills" / SKILL_NAME

CODEX_HOME = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
HOME = Path.home()

CANDIDATES = (
    ("workspace (project-level)", WORKSPACE_SKILL),
    ("CODEX_HOME user skills", CODEX_HOME / "skills" / SKILL_NAME),
    ("HOME .agents user skills", HOME / ".agents" / "skills" / SKILL_NAME),
)


def safe_remove(label: str, target: Path) -> str:
    if target.is_symlink():
        target.unlink()
        return f"removed symlink {target}"
    if target.is_dir():
        shutil.rmtree(target)
        return f"removed dir {target}"
    if target.exists():
        target.unlink()
        return f"removed file {target}"
    return f"not present ({label})"


def main() -> None:
    print(f"Resetting Demo 05 skill '{SKILL_NAME}' (only this skill):")
    for label, target in CANDIDATES:
        print(f"  {label}: {safe_remove(label, target)}")
    print("Done. No parent skills directory or other skills were touched.")


if __name__ == "__main__":
    main()
