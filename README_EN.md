# YYSLS Shifu Skill

> Turn chat logs, screenshots, and personal descriptions of a *Where Winds Meet* mentor into a reusable mentor Skill.

This project is basically a *colleague-skill* style workflow, but the target is not a coworker.  
It is a mentor from the *Where Winds Meet* master-disciple context.

Input:

- WeChat chat logs
- QQ chat logs
- screenshots
- text notes
- your own description of the mentor

Output:

- a new mentor Skill under `masters/{slug}/`

The generated result keeps two things at the same time:

- how this person talks
- how this person guides a disciple through the game

---

## What It Generates

Each generated mentor is split into two parts:

### Part A - Mentor Memory

- how they guide progression
- how they think about early game routing
- how they explain farming, social goals, and master-disciple content
- how they treat goals like outfits, companionship, or efficiency

### Part B - Persona

- how they speak
- whether they are blunt, gentle, sarcastic, or protective
- how they comfort
- how they push progress
- how they react when the disciple messes things up

Final runtime logic:

`receive question -> Persona sets tone -> Mentor Memory gives game guidance -> reply in that person's style`

---

## Supported Inputs

- pasted chat logs
- uploaded text files
- chat screenshots
- subjective descriptions
- mixed materials

If you do not have enough raw material yet, you can still build a first draft and refine it later.

---

## Installation

### Codex

If you use Codex, place the skill under `~/.codex/skills/`:

```bash
git clone <your-repo-or-local-copy> ~/.codex/skills/yysls-shifu
```

For the current local machine setup, you can also copy this local folder directly:

```text
E:\codex\yysls-shifu
```

into:

```text
C:\Users\<your-user>\.codex\skills\yysls-shifu
```

### Claude Code

Project-local:

```bash
mkdir -p .claude/skills
git clone <your-repo-or-local-copy> .claude/skills/yysls-shifu
```

Global:

```bash
git clone <your-repo-or-local-copy> ~/.claude/skills/yysls-shifu
```

### OpenClaw

```bash
git clone <your-repo-or-local-copy> ~/.openclaw/workspace/skills/yysls-shifu
```

---

## Usage

Create a new mentor:

```text
/create-yysls-shifu
```

Then provide:

1. mentor name
2. relationship summary
3. overall impression
4. chat logs / screenshots / notes / descriptions

After generation, call the resulting mentor via:

```text
/{slug}
```

---

## Update Flow

Append more material:

```text
append records
```

Or:

```text
/update-yysls-shifu {slug}
```

Correct the persona:

```text
this is wrong, they would not say it like this
```

---

## Repo Structure

```text
yysls-shifu/
├── SKILL.md
├── README.md
├── README_EN.md
├── INSTALL.md
├── prompts/
├── references/
├── tools/
└── masters/
```

---

## Demo

A demo mentor is included:

- `masters/ajiu-shifu/`

It contains:

- simulated chat logs
- persona file
- mentor memory file
- final generated Skill

---

## In One Sentence

This is a *Where Winds Meet* mentor-distillation Skill builder.
