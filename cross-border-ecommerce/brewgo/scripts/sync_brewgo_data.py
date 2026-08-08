#!/usr/bin/env python3
"""Sync BrewGo Source-of-Truth snapshots into the standalone classroom Demo."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

SOURCE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DEMO_ROOT = SOURCE_ROOT.parents[2] / "Demo" / "brewgo-codex-course"
MANAGED_DIRS = (Path("business"), Path("data/raw"), Path("data/expected"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def managed_files() -> list[Path]:
    files: list[Path] = []
    for relative_dir in MANAGED_DIRS:
        source_dir = SOURCE_ROOT / relative_dir
        if not source_dir.is_dir():
            raise SystemExit(f"Missing source directory: {source_dir}")
        files.extend(path for path in source_dir.rglob("*") if path.is_file())
    return sorted(files)


def validate_target(target: Path) -> Path:
    resolved = target.expanduser().resolve()
    if resolved in {Path("/").resolve(), Path.home().resolve(), SOURCE_ROOT.resolve()}:
        raise SystemExit(f"Unsafe Demo target: {resolved}")
    if resolved.name != "brewgo-codex-course":
        raise SystemExit("Demo target directory must be named brewgo-codex-course")
    return resolved


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo-root", type=Path, default=DEFAULT_DEMO_ROOT)
    parser.add_argument("--reset", action="store_true", help="also replace data/work from the synced expected baseline")
    args = parser.parse_args()
    demo_root = validate_target(args.demo_root)
    if not demo_root.is_dir():
        raise SystemExit(f"Demo project does not exist: {demo_root}")

    copied: list[str] = []
    checksums: dict[str, str] = {}
    for source_file in managed_files():
        relative = source_file.relative_to(SOURCE_ROOT)
        destination = demo_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_file, destination)
        copied.append(relative.as_posix())
        source_hash = sha256(source_file)
        if sha256(destination) != source_hash:
            raise SystemExit(f"Checksum mismatch after copy: {relative}")
        checksums[relative.as_posix()] = source_hash

    version = (SOURCE_ROOT / "VERSION").read_text(encoding="utf-8").strip()
    manifest = {
        "dataset": "BrewGo G2 classroom mock data",
        "dataset_version": version,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_project": "Agent-demo-data/cross-border-ecommerce/brewgo",
        "managed_files": checksums,
    }
    manifest_path = demo_root / "data" / "brewgo_data_manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    if args.reset:
        work = demo_root / "data" / "work"
        if work.exists():
            shutil.rmtree(work)
        shutil.copytree(demo_root / "data" / "expected", work)

    print(f"Synced BrewGo dataset version: {version}")
    for relative in copied:
        print(f"SYNCED {relative}")
    print(f"MANIFEST {manifest_path.relative_to(demo_root)}")
    print("WORK reset from data/expected" if args.reset else "WORK untouched (use --reset to restore it)")
    print("OUTPUTS untouched")


if __name__ == "__main__":
    main()
