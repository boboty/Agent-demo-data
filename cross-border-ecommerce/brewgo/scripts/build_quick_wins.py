#!/usr/bin/env python3
"""Build only the six BrewGo Quick Wins Codex workspaces."""
from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
from pathlib import Path

SOURCE_ROOT = Path(__file__).resolve().parents[1]
CLASSROOM_ROOT = SOURCE_ROOT / "classroom" / "quick-wins"
WORKSPACES_ROOT = SOURCE_ROOT / "workspaces" / "codex"
TARGET_ROOT = WORKSPACES_ROOT / "quick-wins"
TASKS = (
    "01-file-organizer",
    "02-version-diff",
    "03-action-items",
    "04-docs-to-table",
    "05-data-health-check",
    "06-weekly-report",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_snapshot() -> dict[str, str]:
    snapshot: dict[str, str] = {}
    for path in sorted(CLASSROOM_ROOT.rglob("*")):
        if path.is_symlink():
            raise SystemExit(f"Quick Wins source must not contain symlinks: {path}")
        if path.is_file():
            snapshot[path.relative_to(CLASSROOM_ROOT).as_posix()] = sha256(path)
    return snapshot


def preflight() -> None:
    if not CLASSROOM_ROOT.is_dir() or CLASSROOM_ROOT.is_symlink():
        raise SystemExit(f"Missing or unsafe Quick Wins source: {CLASSROOM_ROOT}")
    expected_target = WORKSPACES_ROOT / "quick-wins"
    if TARGET_ROOT != expected_target or TARGET_ROOT.parent.resolve() != WORKSPACES_ROOT.resolve():
        raise SystemExit(f"Unsafe Quick Wins target: {TARGET_ROOT}")
    if TARGET_ROOT.is_symlink():
        raise SystemExit(f"Refusing to replace symlink target: {TARGET_ROOT}")
    for task in TASKS:
        task_root = CLASSROOM_ROOT / task
        required = (
            task_root / "README.md",
            task_root / "INSTRUCTOR_COPY_PROMPT.md",
            task_root / "EXPECTED.md",
            task_root / "input",
            task_root / "outputs",
        )
        for path in required:
            if path.is_symlink() or not path.exists():
                raise SystemExit(f"Missing or unsafe Quick Win asset: {path}")
        if not (task_root / "input").is_dir() or not any(
            path.is_file() for path in (task_root / "input").rglob("*")
        ):
            raise SystemExit(f"Quick Win input must not be empty: {task_root / 'input'}")
        output_entries = [p for p in (task_root / "outputs").iterdir() if p.name != ".gitkeep"]
        if output_entries:
            raise SystemExit(f"Classroom outputs must be empty: {task_root / 'outputs'}")


def build_task(task: str, staging_root: Path, version: str) -> None:
    source = CLASSROOM_ROOT / task
    destination = staging_root / task
    destination.mkdir(parents=True)
    shutil.copy2(source / "README.md", destination / "README.md")
    shutil.copytree(source / "input", destination / "input")
    (destination / "outputs").mkdir()

    generated: dict[str, str] = {}
    for path in sorted(destination.rglob("*")):
        if path.is_symlink():
            raise SystemExit(f"Generated workspace contains a symlink: {path}")
        if path.is_file():
            generated[path.relative_to(destination).as_posix()] = sha256(path)

    manifest = {
        "workspace": f"brewgo/codex/quick-wins/{task}",
        "task": task,
        "data_version": version,
        "source": f"classroom/quick-wins/{task}",
        "generated_files": generated,
        "outputs_initially_empty": True,
    }
    (destination / "workspace-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def replace_target(staging_root: Path) -> None:
    if TARGET_ROOT.exists():
        if TARGET_ROOT.is_symlink() or not TARGET_ROOT.is_dir():
            raise SystemExit(f"Unsafe existing Quick Wins target: {TARGET_ROOT}")
        shutil.rmtree(TARGET_ROOT)
    shutil.move(str(staging_root), TARGET_ROOT)


def main() -> None:
    preflight()
    before = source_snapshot()
    version = (SOURCE_ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not version:
        raise SystemExit("VERSION must not be empty")

    WORKSPACES_ROOT.mkdir(parents=True, exist_ok=True)
    temporary_parent = Path(tempfile.mkdtemp(prefix=".quick-wins-build-", dir=WORKSPACES_ROOT))
    staging_root = temporary_parent / "quick-wins"
    staging_root.mkdir()
    try:
        for task in TASKS:
            build_task(task, staging_root, version)
        if source_snapshot() != before:
            raise SystemExit("Classroom Quick Wins source changed during build")
        replace_target(staging_root)
    finally:
        if temporary_parent.exists():
            shutil.rmtree(temporary_parent)

    print(f"BrewGo Quick Wins workspaces rebuilt; data_version={version}")
    for task in TASKS:
        file_count = sum(1 for path in (TARGET_ROOT / task / "input").rglob("*") if path.is_file())
        print(f"BUILT {task}: input_files={file_count}, outputs_empty=True")


if __name__ == "__main__":
    main()
