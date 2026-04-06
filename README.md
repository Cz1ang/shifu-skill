# 师父 skill / Shifu Skill

> 把微信、QQ、截图、文本里的《燕云十六声》师父聊天材料，蒸馏成一个可调用、可持续进化的师父 skill / shifu skill。

**关键词**：师父 skill、shifu skill、燕云十六声师父、燕云师父 skill

[![Skill](https://img.shields.io/badge/Skill-YYSLS%20Shifu-blue)](#)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](#)

你的燕云师父退游了、A 了、懒得回你了，或者你只是想把那个“会带你、会骂你两句、但最后还是会回来收拾残局”的人留下来？

这个仓库做的事很简单：

- 输入聊天记录、截图、文本和你的主观描述
- 提取他的 `带徒思路` 和 `说话方式`
- 生成一个新的师父 Skill

整体工作流参考 `同事.skill`，只是把对象从“同事”换成了“燕云师徒关系里的师父”。

---

## 它能做什么

这个 skill 生成出来的实例，不只是“像他说话”，也不只是“会讲燕云攻略”。

它会拆成两部分：

- **Part A - Mentor Memory**
  - 他怎么带燕云
  - 怎么安排开荒、跑图、养成、社交玩法
  - 怎么看师徒、双飞燕、桃李值、和合花钱这类问题
- **Part B - Persona**
  - 他怎么说话
  - 会不会嘴硬
  - 怎么安慰人
  - 怎么催进度
  - 徒弟玩崩了他会怎么收

最终运行逻辑：

`收到问题 -> 先决定语气 -> 再给燕云建议 -> 用他的方式输出`

---

## 支持的输入

- 微信聊天记录
- QQ 聊天记录
- 聊天截图
- 手动整理的文本
- 你自己写的“师父画像”
- 混合材料

如果你现在没有完整聊天记录，也可以先只靠主观描述做第一版，后面再追加材料迭代。

---

## 推荐的聊天记录提取工具

参考 `前任skill` 的做法，这里补一组可直接放进导出流程的工具链接。

### 微信

- [LC044/WeChatMsg](https://github.com/LC044/WeChatMsg)
  - Windows 端常见微信聊天记录导出工具，社区使用面较广
- [lqzhgood/Shmily](https://github.com/lqzhgood/Shmily)
  - 可做多平台聊天记录归档，适合把导出后的聊天进一步整理

说明：

- 之前社区常提到的 `PyWxDump` 目前公开仓库已经移除，不建议再把它写成主推荐项
- 如果你已经能导出成 `txt / html / json / 截图`，直接喂给本项目就行，不强依赖某一个工具

### QQ

- [Yiyiyimu/QQ-History-Backup](https://github.com/Yiyiyimu/QQ-History-Backup)
  - QQ 聊天记录备份导出，适合做原始记录导出
- [QQBackup/qq-win-db-key](https://github.com/QQBackup/qq-win-db-key)
  - 更偏进阶，适合需要处理 QQ 数据库解密的场景
- [lqzhgood/Shmily](https://github.com/lqzhgood/Shmily)
  - 如果你已经拿到 QQ 导出文本，也可以再用它做统一归档

说明：

- QQ 导出生态没有微信那么统一，最稳的方式仍然是：能导出文本就导文本，导不出来就截图
- 这个项目真正需要的是“可读的聊天材料”，不是强绑定某个导出器

---

## 安装

### Codex

如果你用的是 Codex，把 skill 放到 `~/.codex/skills/` 下即可。

如果你当前就是在这台机器上本地使用这份目录，直接把：

```text
E:\codex\yysls-shifu
```

复制到：

```text
C:\Users\你的用户名\.codex\skills\yysls-shifu
```

如果后面你把它放到 Git 仓库，再用：

```bash
git clone <your-repo-or-local-copy> ~/.codex/skills/yysls-shifu
```

Windows 通常对应：

```text
C:\Users\你的用户名\.codex\skills\yysls-shifu
```

### Claude Code

在你的项目根目录执行：

```bash
mkdir -p .claude/skills
git clone <your-repo-or-local-copy> .claude/skills/yysls-shifu
```

如果你现在只是本地使用，也可以直接把：

```text
E:\codex\yysls-shifu
```

复制到你的项目目录：

```text
你的项目\.claude\skills\yysls-shifu
```

或者装到全局：

```bash
git clone <your-repo-or-local-copy> ~/.claude/skills/yysls-shifu
```

### OpenClaw

```bash
git clone <your-repo-or-local-copy> ~/.openclaw/workspace/skills/yysls-shifu
```

如果只是在本地直接放置目录，也可以把：

```text
E:\codex\yysls-shifu
```

复制到：

```text
~/.openclaw/workspace/skills/yysls-shifu
```

---

## 使用

### 1. 创建一个新师父

在支持 skill 的环境里输入：

```text
/create-yysls-shifu
```

然后按流程提供：

1. 师父称呼
2. 你们的关系
3. 你对他的印象
4. 聊天记录 / 截图 / 文本 / 主观描述

完成后会生成一个实例目录：

```text
masters/{slug}/
  SKILL.md
  persona.md
  mentor_memory.md
  meta.json
  versions/
  knowledge/
```

### 2. 调用生成好的师父

生成完成后，直接用：

```text
/{slug}
```

### 3. 追加新材料

你后面拿到新的聊天记录或截图时，可以继续更新：

```text
追加记录
```

或者：

```text
/update-yysls-shifu {slug}
```

### 4. 纠正人设

如果结果不像他，直接说：

```text
这不对，他不会这么说
```

或：

```text
他其实更像……
```

---

## 管理命令

列出已有师父：

```bash
python tools/skill_writer.py --action list --base-dir ./masters
```

备份版本：

```bash
python tools/version_manager.py --action backup --slug {slug} --base-dir ./masters
```

查看版本：

```bash
python tools/version_manager.py --action list --slug {slug} --base-dir ./masters
```

回滚版本：

```bash
python tools/version_manager.py --action rollback --slug {slug} --version {version} --base-dir ./masters
```

---

## 目录结构

```text
yysls-shifu/
├── SKILL.md
├── README.md
├── prompts/
│   ├── intake.md
│   ├── chat_analyzer.md
│   ├── persona_analyzer.md
│   ├── persona_builder.md
│   ├── merger.md
│   └── correction_handler.md
├── references/
│   ├── source-ingest.md
│   └── yysls-shifu-archetype.md
├── tools/
│   ├── skill_writer.py
│   └── version_manager.py
└── masters/
    └── ajiu-shifu/
```

---

## 示例实例

仓库里已经放了一个 demo：

- `masters/ajiu-shifu/`

里面有：

- 模拟聊天样本
- 人设文件
- 带徒记忆文件
- 最终生成出来的实例 Skill

这个 demo 的定位是：

- 嘴上有点损
- 讲话不长
- 会说“别”“先别”“截图发我”
- 关键时候会回来兜底

你可以把它当成模板，再替换成你自己的真实材料。

---

## 适合什么场景

- 你想把某个燕云师父做成长期可用的人格
- 你希望它既保留聊天味，又保留带图思路
- 你没有特别完整的材料，想先做一版再慢慢修
- 你想做的是“师父人格”，不是泛用燕云攻略机器人

---

## 注意

- 这套东西更像“蒸馏器”，不是现成师父 prompt
- 真正的质量取决于原材料质量
- 聊天越真实、越有带图内容、越有情绪波动，最后越像真人
- 如果只有一句“他很温柔会带我”，那只能先做低样本版

---
