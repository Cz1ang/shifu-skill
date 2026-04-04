#!/usr/bin/env python3
import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path


FILES = ["SKILL.md", "persona.md", "mentor_memory.md", "meta.json"]


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def backup(root: Path) -> None:
    versions = root / "versions"
    versions.mkdir(parents=True, exist_ok=True)
    version = datetime.now().strftime("v%Y%m%d-%H%M%S")
    target = versions / version
    target.mkdir(parents=True, exist_ok=False)
    for name in FILES:
        src = root / name
        if src.exists():
            shutil.copy2(src, target / name)
    print(version)


def list_versions(root: Path) -> None:
    versions = root / "versions"
    if not versions.exists():
        print("no versions")
        return
    for item in sorted(versions.iterdir()):
        if item.is_dir():
            print(item.name)


def rollback(root: Path, version: str) -> None:
    source = root / "versions" / version
    if not source.exists():
        raise SystemExit(f"version not found: {version}")
    for name in FILES:
        src = source / name
        if src.exists():
            shutil.copy2(src, root / name)

    meta_path = root / "meta.json"
    if meta_path.exists():
        meta = json.loads(load_text(meta_path))
        meta["version"] = version
        meta["updated_at"] = datetime.now().isoformat(timespec="seconds")
        write_text(meta_path, json.dumps(meta, ensure_ascii=False, indent=2))

    print(f"rolled back to {version}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", required=True, choices=["backup", "list", "rollback"])
    parser.add_argument("--slug", required=True)
    parser.add_argument("--base-dir", required=True)
    parser.add_argument("--version")
    args = parser.parse_args()

    root = Path(args.base_dir) / args.slug

    if args.action == "backup":
        backup(root)
    elif args.action == "list":
        list_versions(root)
    elif args.action == "rollback":
        if not args.version:
            raise SystemExit("--version is required for rollback")
        rollback(root, args.version)


if __name__ == "__main__":
    main()
