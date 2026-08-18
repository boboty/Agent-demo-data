#!/usr/bin/env python3
"""Build only the three BrewGo Day2 Live Tasks Codex workspaces."""
from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
import zipfile
from pathlib import Path

SOURCE_ROOT = Path(__file__).resolve().parents[1]
CLASSROOM_ROOT = SOURCE_ROOT / "classroom" / "day2-live-tasks"
WORKSPACES_ROOT = SOURCE_ROOT / "workspaces" / "codex"
TARGET_ROOT = WORKSPACES_ROOT / "day2-live-tasks"
TASKS = (
    "01-amazon-competitor-discovery",
    "02-instagram-lead-discovery",
    "03-data-analysis-dashboard",
)
STUDENT_FILES = ("README.md", "RAW_REQUEST.md")
TEACHING_LABELS = (b"FICTIONAL / TEACHING SNAPSHOT", b"FICTIONAL / TEACHING DATASET")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def snapshot(root: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    if not root.exists():
        return result
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise SystemExit(f"Source must not contain symlinks: {path}")
        if path.is_file():
            result[path.relative_to(root).as_posix()] = sha256(path)
    return result


def protected_demo_snapshot() -> dict[str, str]:
    protected: dict[str, str] = {}
    patterns = (
        (SOURCE_ROOT / "classroom", "0[1-7]-*"),
        (WORKSPACES_ROOT, "0[1-7]-*"),
        (SOURCE_ROOT / "instructor", "demo-0*"),
    )
    for base, pattern in patterns:
        for root in sorted(base.glob(pattern)):
            if root.is_file():
                protected[root.relative_to(SOURCE_ROOT).as_posix()] = sha256(root)
            elif root.is_dir():
                for path in sorted(root.rglob("*")):
                    if path.is_file():
                        protected[path.relative_to(SOURCE_ROOT).as_posix()] = sha256(path)
    return protected


def xlsx_contains_label(path: Path) -> bool:
    try:
        with zipfile.ZipFile(path) as archive:
            payload = b"".join(
                archive.read(name)
                for name in archive.namelist()
                if name.endswith(".xml")
            )
    except zipfile.BadZipFile as exc:
        raise SystemExit(f"Invalid xlsx fixture: {path}: {exc}") from exc
    return any(label in payload for label in TEACHING_LABELS)


def assert_empty_output(output: Path) -> None:
    if output.is_symlink() or not output.is_dir():
        raise SystemExit(f"Missing or unsafe classroom output directory: {output}")
    entries = [path for path in output.iterdir() if path.name != ".gitkeep"]
    if entries:
        raise SystemExit(f"Classroom outputs must be empty: {output}")


def preflight() -> None:
    expected_target = WORKSPACES_ROOT / "day2-live-tasks"
    if TARGET_ROOT != expected_target or TARGET_ROOT.parent.resolve() != WORKSPACES_ROOT.resolve():
        raise SystemExit(f"Unsafe Day2 target: {TARGET_ROOT}")
    if not CLASSROOM_ROOT.is_dir() or CLASSROOM_ROOT.is_symlink():
        raise SystemExit(f"Missing or unsafe Day2 source: {CLASSROOM_ROOT}")
    common_rules = CLASSROOM_ROOT / "WORKSPACE_RULES.md"
    if common_rules.is_symlink() or not common_rules.is_file():
        raise SystemExit(f"Missing common workspace rules: {common_rules}")
    for task in TASKS:
        task_root = CLASSROOM_ROOT / task
        if task_root.is_symlink() or not task_root.is_dir():
            raise SystemExit(f"Missing or unsafe Day2 task: {task_root}")
        for name in (*STUDENT_FILES, "INSTRUCTOR_GUIDE.md"):
            path = task_root / name
            if path.is_symlink() or not path.is_file():
                raise SystemExit(f"Missing task asset: {path}")
        input_root = task_root / "input"
        if input_root.is_symlink() or not input_root.is_dir() or not any(path.is_file() for path in input_root.rglob("*")):
            raise SystemExit(f"Task input must contain files: {input_root}")
        assert_empty_output(task_root / "outputs")

    amazon = CLASSROOM_ROOT / TASKS[0] / "input" / "offline"
    amazon_html = sorted(amazon.rglob("*.html"))
    if len(amazon_html) != 13:
        raise SystemExit(f"Amazon Offline must contain 13 HTML snapshots, found {len(amazon_html)}")
    instagram = CLASSROOM_ROOT / TASKS[1] / "input" / "offline"
    instagram_html = sorted(instagram.rglob("*.html"))
    if len(instagram_html) != 19:
        raise SystemExit(f"Instagram Offline must contain 19 HTML snapshots, found {len(instagram_html)}")
    for path in (*amazon_html, *instagram_html):
        if TEACHING_LABELS[0] not in path.read_bytes():
            raise SystemExit(f"Teaching snapshot label missing: {path}")
    workbook = CLASSROOM_ROOT / TASKS[2] / "input" / "business-performance.xlsx"
    if not workbook.is_file() or not xlsx_contains_label(workbook):
        raise SystemExit(f"Teaching workbook label missing: {workbook}")


def build_task(task: str, staging_root: Path, version: str) -> None:
    source = CLASSROOM_ROOT / task
    destination = staging_root / task
    destination.mkdir(parents=True)
    for name in STUDENT_FILES:
        shutil.copy2(source / name, destination / name)
    # Codex loads AGENTS.md automatically; keep the public source name tool-neutral.
    shutil.copy2(CLASSROOM_ROOT / "WORKSPACE_RULES.md", destination / "AGENTS.md")
    shutil.copytree(source / "input", destination / "input")
    output = destination / "outputs"
    output.mkdir()
    (output / ".gitkeep").write_text("", encoding="utf-8")

    forbidden = list(destination.rglob("INSTRUCTOR_GUIDE.md")) + list(destination.rglob("SKILL.md"))
    forbidden += [path for path in destination.rglob(".agents")]
    if forbidden:
        raise SystemExit(f"Instructor or final Skill leaked into {task}: {forbidden}")

    generated: dict[str, str] = {}
    for path in sorted(destination.rglob("*")):
        if path.is_symlink():
            raise SystemExit(f"Generated workspace contains a symlink: {path}")
        if path.is_file():
            generated[path.relative_to(destination).as_posix()] = sha256(path)
    manifest = {
        "workspace": f"brewgo/codex/day2-live-tasks/{task}",
        "task": task,
        "data_version": version,
        "source": f"classroom/day2-live-tasks/{task}",
        "generated_files": generated,
        "outputs_initially_empty": True,
        "instructor_assets_excluded": True,
        "final_skill_preinstalled": False,
    }
    (destination / "workspace-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def replace_target(staging_root: Path) -> None:
    if TARGET_ROOT.exists():
        if TARGET_ROOT.is_symlink() or not TARGET_ROOT.is_dir():
            raise SystemExit(f"Unsafe existing Day2 target: {TARGET_ROOT}")
        shutil.rmtree(TARGET_ROOT)
    shutil.move(str(staging_root), TARGET_ROOT)


def verify_generated() -> None:
    if tuple(sorted(path.name for path in TARGET_ROOT.iterdir() if path.is_dir())) != TASKS:
        raise SystemExit("Generated task whitelist mismatch")
    for task in TASKS:
        root = TARGET_ROOT / task
        output_entries = [path for path in (root / "outputs").iterdir() if path.name != ".gitkeep"]
        if output_entries:
            raise SystemExit(f"Generated outputs not empty: {root / 'outputs'}")
        manifest = json.loads((root / "workspace-manifest.json").read_text(encoding="utf-8"))
        if not manifest.get("outputs_initially_empty") or not manifest.get("instructor_assets_excluded"):
            raise SystemExit(f"Generated manifest contract failed: {task}")
        if list(root.rglob("INSTRUCTOR_GUIDE.md")) or list(root.rglob("SKILL.md")) or list(root.rglob(".agents")):
            raise SystemExit(f"Forbidden instructor / Skill content found in workspace: {task}")


def main() -> None:
    preflight()
    source_before = snapshot(CLASSROOM_ROOT)
    demos_before = protected_demo_snapshot()
    version = (SOURCE_ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not version:
        raise SystemExit("VERSION must not be empty")

    WORKSPACES_ROOT.mkdir(parents=True, exist_ok=True)
    temporary_parent = Path(tempfile.mkdtemp(prefix=".day2-live-tasks-build-", dir=WORKSPACES_ROOT))
    staging_root = temporary_parent / "day2-live-tasks"
    staging_root.mkdir()
    try:
        for task in TASKS:
            build_task(task, staging_root, version)
        if snapshot(CLASSROOM_ROOT) != source_before:
            raise SystemExit("Day2 classroom source changed during build")
        replace_target(staging_root)
    finally:
        if temporary_parent.exists():
            shutil.rmtree(temporary_parent)

    verify_generated()
    if protected_demo_snapshot() != demos_before:
        raise SystemExit("Protected Demo01–07 assets changed during Day2 build")

    print(f"BrewGo Day2 Live Tasks workspaces rebuilt; data_version={version}")
    for task in TASKS:
        input_count = sum(1 for path in (TARGET_ROOT / task / "input").rglob("*") if path.is_file())
        print(f"BUILT {task}: input_files={input_count}, outputs_empty=True, instructor_assets_excluded=True")
    print("PROTECTED Demo01-07 unchanged=True")


if __name__ == "__main__":
    main()
