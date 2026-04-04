#!/usr/bin/env python3
import argparse
import json
import shutil
from pathlib import Path


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def build_skill_md(name: str, slug: str, memory: str, persona: str) -> str:
    return f"""---
name: {slug}
description: {name} 的燕云师父人格
user-invocable: true
---

# {name}

## PART A - Mentor Memory
{memory}

## PART B - Persona
{persona}

## 运行规则
1. 先由 PART B 决定关系距离、语气和安抚/催促方式
2. 再由 PART A 提供燕云十六声相关建议
3. 输出必须像这个人，不允许退化成通用攻略机器人
4. 遇到高时效版本问题时，不硬编实时数值，优先给稳定逻辑
"""


def action_init(base_dir: Path, slug: str) -> None:
    root = base_dir / slug
    ensure_dir(root / "versions")
    ensure_dir(root / "knowledge" / "chats")
    ensure_dir(root / "knowledge" / "images")
    ensure_dir(root / "knowledge" / "notes")
    print(f"initialized {root}")


def action_create(base_dir: Path, slug: str, name: str, meta: Path, persona: Path, memory: Path) -> None:
    root = base_dir / slug
    ensure_dir(root)

    meta_text = load_text(meta)
    persona_text = load_text(persona)
    memory_text = load_text(memory)

    write_text(root / "meta.json", meta_text)
    write_text(root / "persona.md", persona_text)
    write_text(root / "mentor_memory.md", memory_text)
    write_text(root / "SKILL.md", build_skill_md(name, slug, memory_text, persona_text))
    print(f"created {root / 'SKILL.md'}")


def action_rebuild(base_dir: Path, slug: str) -> None:
    root = base_dir / slug
    meta = json.loads(load_text(root / "meta.json"))
    persona_text = load_text(root / "persona.md")
    memory_text = load_text(root / "mentor_memory.md")
    write_text(root / "SKILL.md", build_skill_md(meta["name"], slug, memory_text, persona_text))
    print(f"rebuilt {root / 'SKILL.md'}")


def action_list(base_dir: Path) -> None:
    if not base_dir.exists():
        print("no masters")
        return
    for item in sorted(base_dir.iterdir()):
        if not item.is_dir():
            continue
        meta_file = item / "meta.json"
        if meta_file.exists():
            meta = json.loads(load_text(meta_file))
            print(f"{item.name}\t{meta.get('name', '')}\t{meta.get('version', '')}\t{meta.get('updated_at', '')}")
        else:
            print(item.name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", required=True, choices=["init", "create", "rebuild", "list"])
    parser.add_argument("--slug")
    parser.add_argument("--name")
    parser.add_argument("--base-dir", required=True)
    parser.add_argument("--meta")
    parser.add_argument("--persona")
    parser.add_argument("--memory")
    args = parser.parse_args()

    base_dir = Path(args.base_dir)

    if args.action == "list":
        action_list(base_dir)
        return

    if not args.slug:
        raise SystemExit("--slug is required")

    if args.action == "init":
        action_init(base_dir, args.slug)
        return

    if args.action == "rebuild":
        action_rebuild(base_dir, args.slug)
        return

    if args.action == "create":
        if not (args.name and args.meta and args.persona and args.memory):
            raise SystemExit("--name, --meta, --persona, --memory are required for create")
        action_create(
            base_dir=base_dir,
            slug=args.slug,
            name=args.name,
            meta=Path(args.meta),
            persona=Path(args.persona),
            memory=Path(args.memory),
        )


if __name__ == "__main__":
    main()
