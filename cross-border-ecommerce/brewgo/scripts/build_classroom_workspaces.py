#!/usr/bin/env python3
"""Build isolated Codex classroom workspaces from BrewGo public assets."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
from pathlib import Path

SOURCE_ROOT = Path(__file__).resolve().parents[1]
WORKSPACES_ROOT = SOURCE_ROOT / "workspaces" / "codex"
STAGE_NAMES = (
    "01-direct-task",
    "02-task-card",
    "03-project-context",
    "04-fba-profit-calculator",
    "05-search-term-skill",
    "06-competitor-listing-optimization",
)

COMMON_INPUTS = (
    (Path("data/raw/listing_current.md"), Path("input/listing_current.md")),
    (Path("business/product_profile_g2.md"), Path("input/product_profile_g2.md")),
    (Path("data/raw/products.xlsx"), Path("input/products.xlsx")),
    (Path("data/raw/reviews.csv"), Path("input/reviews.csv")),
)

BUSINESS_SNAPSHOT = (
    (Path("business/store_profile.md"), Path("business/store_profile.md")),
    (Path("business/product_profile_g2.md"), Path("business/product_profile_g2.md")),
    (Path("business/brand_rules.md"), Path("business/brand_rules.md")),
    (Path("business/business_rules.md"), Path("business/business_rules.md")),
    (Path("business/field_dictionary.md"), Path("business/field_dictionary.md")),
)

FBA_INPUTS = (
    (Path("data/raw/products.xlsx"), Path("input/products.xlsx")),
    (Path("data/raw/cost_parameters.xlsx"), Path("input/cost_parameters.xlsx")),
)

SEARCH_TERM_INPUTS = (
    (
        Path("classroom/05-search-term-skill/input/history/search_terms_history.xlsx"),
        Path("input/history/search_terms_history.xlsx"),
    ),
    (
        Path("classroom/05-search-term-skill/input/next-period/search_terms_latest.xlsx"),
        Path("input/next-period/search_terms_latest.xlsx"),
    ),
)

STAGE_ASSETS = {
    "01-direct-task": (
        (Path("classroom/01-direct-task/task.md"), Path("task.md")),
        *COMMON_INPUTS,
    ),
    "02-task-card": (
        *COMMON_INPUTS,
    ),
    "03-project-context": (
        (Path("classroom/03-project-context/project-context.md"), Path("project-context.md")),
        (Path("adapters/codex/AGENTS.md.template"), Path("AGENTS.md")),
        *BUSINESS_SNAPSHOT,
        *COMMON_INPUTS,
    ),
    "04-fba-profit-calculator": (
        (Path("classroom/03-project-context/project-context.md"), Path("project-context.md")),
        (Path("classroom/04-fba-profit-calculator/profit-rules.md"), Path("profit-rules.md")),
        (Path("adapters/codex/AGENTS.md.fba-profit.template"), Path("AGENTS.md")),
        *BUSINESS_SNAPSHOT,
        *FBA_INPUTS,
    ),
    "05-search-term-skill": (
        (Path("classroom/03-project-context/project-context.md"), Path("project-context.md")),
        (Path("adapters/codex/AGENTS.md.search-term-skill.template"), Path("AGENTS.md")),
        *BUSINESS_SNAPSHOT,
        *SEARCH_TERM_INPUTS,
    ),
    "06-competitor-listing-optimization": (
        (Path("classroom/03-project-context/project-context.md"), Path("project-context.md")),
        (Path("adapters/codex/AGENTS.md.template"), Path("AGENTS.md")),
        (Path("classroom/06-competitor-listing-optimization/task.md"), Path("task.md")),
        (Path("classroom/06-competitor-listing-optimization/report-template.html"), Path("report-template.html")),
        *BUSINESS_SNAPSHOT,
        *COMMON_INPUTS,
    ),
}

# Directories created empty (with a .gitkeep marker) in each stage's workspace.
STAGE_EMPTY_DIRS = {
    "01-direct-task": ("outputs",),
    "02-task-card": ("outputs",),
    "03-project-context": ("outputs",),
    "04-fba-profit-calculator": ("outputs",),
    "05-search-term-skill": ("outputs/first-run", "outputs/second-run", ".agents/skills"),
    "06-competitor-listing-optimization": ("outputs",),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_relative(path: Path, label: str) -> None:
    if path.is_absolute() or ".." in path.parts:
        raise SystemExit(f"Unsafe {label} path: {path}")


def preflight() -> None:
    if tuple(STAGE_ASSETS) != STAGE_NAMES:
        raise SystemExit("Stage asset map must exactly match the approved stage whitelist")
    if tuple(STAGE_EMPTY_DIRS) != STAGE_NAMES:
        raise SystemExit("Stage empty-dir map must exactly match the approved stage whitelist")
    if WORKSPACES_ROOT.is_symlink():
        raise SystemExit(f"Workspace root must not be a symlink: {WORKSPACES_ROOT}")
    for stage, assets in STAGE_ASSETS.items():
        if stage not in STAGE_NAMES:
            raise SystemExit(f"Unapproved stage: {stage}")
        destinations: set[Path] = set()
        for source_relative, destination_relative in assets:
            validate_relative(source_relative, "source")
            validate_relative(destination_relative, "destination")
            if destination_relative in destinations:
                raise SystemExit(f"Duplicate destination in {stage}: {destination_relative}")
            destinations.add(destination_relative)
            source = SOURCE_ROOT / source_relative
            if source.is_symlink() or not source.is_file():
                raise SystemExit(f"Missing or unsupported source file: {source}")
    for stage, empty_dirs in STAGE_EMPTY_DIRS.items():
        seen: set[Path] = set()
        for relative in empty_dirs:
            validate_relative(Path(relative), "empty dir")
            if Path(relative) in seen:
                raise SystemExit(f"Duplicate empty dir in {stage}: {relative}")
            seen.add(Path(relative))
    version_file = SOURCE_ROOT / "VERSION"
    if version_file.is_symlink() or not version_file.is_file():
        raise SystemExit(f"Missing or unsupported VERSION file: {version_file}")


def build_stage(stage: str, temporary_root: Path, version: str) -> None:
    stage_root = temporary_root / stage
    stage_root.mkdir()
    copied: dict[str, str] = {}

    for source_relative, destination_relative in STAGE_ASSETS[stage]:
        source = SOURCE_ROOT / source_relative
        destination = stage_root / destination_relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        copied[destination_relative.as_posix()] = sha256(destination)

    for relative in STAGE_EMPTY_DIRS[stage]:
        empty_dir = stage_root / relative
        empty_dir.mkdir(parents=True, exist_ok=True)
        marker = empty_dir / ".gitkeep"
        marker.write_text("", encoding="utf-8")
        copied[f"{relative}/.gitkeep"] = sha256(marker)

    manifest = {
        "workspace": f"brewgo/codex/{stage}",
        "stage": stage,
        "data_version": version,
        "source": "Agent-demo-data/cross-border-ecommerce/brewgo",
        "generated_files": dict(sorted(copied.items())),
    }
    manifest_path = stage_root / "workspace-manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    for path in stage_root.rglob("*"):
        if path.is_symlink():
            raise SystemExit(f"Generated workspace contains a symlink: {path}")


def approved_target(stage: str) -> Path:
    if stage not in STAGE_NAMES:
        raise SystemExit(f"Refusing to clean unapproved stage: {stage}")
    target = WORKSPACES_ROOT / stage
    if target.parent.resolve() != WORKSPACES_ROOT.resolve() or target.name != stage:
        raise SystemExit(f"Unsafe workspace target: {target}")
    return target


def replace_stage(stage: str, temporary_root: Path) -> None:
    target = approved_target(stage)
    if target.is_symlink():
        target.unlink()
    elif target.exists():
        if not target.is_dir():
            raise SystemExit(f"Workspace target is not a directory: {target}")
        shutil.rmtree(target)
    shutil.move(str(temporary_root / stage), target)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--stage",
        action="append",
        choices=STAGE_NAMES,
        help="build only this approved stage; repeat for multiple stages (default: all)",
    )
    args = parser.parse_args()
    preflight()
    selected_stages = tuple(args.stage) if args.stage else STAGE_NAMES
    version = (SOURCE_ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if not version:
        raise SystemExit("VERSION must not be empty")

    WORKSPACES_ROOT.mkdir(parents=True, exist_ok=True)
    temporary_root = Path(tempfile.mkdtemp(prefix=".build-", dir=WORKSPACES_ROOT))
    try:
        for stage in selected_stages:
            build_stage(stage, temporary_root, version)
        for stage in selected_stages:
            replace_stage(stage, temporary_root)
    finally:
        if temporary_root.exists():
            shutil.rmtree(temporary_root)

    print(f"BrewGo classroom workspaces rebuilt; data_version={version}")
    for stage in selected_stages:
        stage_root = approved_target(stage)
        print(f"BUILT {stage}")
        for path in sorted(stage_root.rglob("*")):
            kind = "DIR " if path.is_dir() else "FILE"
            print(f"  {kind} {path.relative_to(stage_root).as_posix()}")


if __name__ == "__main__":
    main()
