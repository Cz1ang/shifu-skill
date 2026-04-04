---
name: yysls-shifu
description: 把微信、QQ、截图、文本里的《燕云十六声》师父聊天材料蒸馏成一个可调用的师父 Skill。整体工作流参考同事.skill，但目标从“同事”改成“燕云师徒关系里的师父”。
---

# 燕云师父.skill 创建器

这个 skill 本质上就是 `同事.skill` 的燕云师徒版。

输入：

- 微信 / QQ 聊天记录
- 聊天截图
- 你自己写的师父画像
- 任何能体现“这个师父怎么带人、怎么说话、怎么安排燕云路线”的材料

输出：

- 一个新的师父 Skill，写到 `masters/{slug}/`
- 这个 Skill 既保留他的说话方式，也保留他的燕云带徒思路

整体结构只有两部分：

- `Part A - Mentor Memory`
  - 他怎么带燕云
  - 他怎么安排开荒、跑图、日常、社交目标
  - 他对师徒、双飞燕、社交玩法怎么理解
- `Part B - Persona`
  - 他怎么说话
  - 他怎么安慰人
  - 他怎么催进度
  - 他嘴硬不嘴硬，会不会损人，会不会兜底

最终运行逻辑：

`收到问题 -> 先用 Persona 决定语气 -> 再用 Mentor Memory 给燕云建议 -> 用他的方式输出`

---

## 触发方式

当用户说这些时启动创建流程：

- `/create-yysls-shifu`
- “帮我做一个燕云师父 skill”
- “蒸馏一个燕云师父”
- “把我师父做成 skill”

当用户说这些时进入更新流程：

- “追加记录”
- “我有新聊天”
- “这不对，他不会这么说”
- `/update-yysls-shifu {slug}`

当用户说 `/list-yysls-shifus` 时列出已有师父 Skill。

---

## Step 1：基础录入

参考 `prompts/intake.md`，只问 3 个问题：

1. 师父怎么称呼
2. 你们是什么关系
3. 他给你的感觉是什么样

收完后先给用户一个简短摘要，确认没问题再继续。

---

## Step 2：导入材料

让用户从下面几种方式里选：

```text
[A] 直接粘贴聊天记录
[B] 上传文本文件
[C] 上传聊天截图
[D] 粘贴你的主观描述
[E] 混合提供
[F] 先跳过，只做第一版
```

处理原则很简单：

- 微信 / QQ 文本直接读
- 截图先转成文字再分析
- 群聊只重点看目标师父自己的发言
- 如果材料很多，优先保留“带图、指路、安慰、催进度、纠错、讲社交玩法”的内容

如需细看来源规则，读取 [references/source-ingest.md](references/source-ingest.md)。

---

## Step 3：分析

参考以下 prompt：

- `prompts/chat_analyzer.md`
- `prompts/persona_analyzer.md`
- `prompts/persona_builder.md`

分析目标只有两个：

1. 提取这个师父的 `Mentor Memory`
2. 提取这个师父的 `Persona`

注意：

- 不要只提炼成“通用燕云攻略”
- 也不要只提炼成“会说话的人设壳子”
- 必须同时保留“他怎么带你玩”和“他怎么对你说”

---

## Step 4：预览

给用户看三块内容：

```text
[Mentor Memory 摘要]
[Persona 摘要]
[3 段示例回复]
```

示例回复建议用这些场景：

- “师父我今天干嘛”
- “师父双飞燕怎么刷”
- “师父我玩乱了”

然后让用户选：

- 直接生成
- 继续调整

---

## Step 5：写入文件

确认后写入：

- `masters/{slug}/mentor_memory.md`
- `masters/{slug}/persona.md`
- `masters/{slug}/meta.json`
- `masters/{slug}/SKILL.md`

写入命令：

```bash
python tools/skill_writer.py --action init --slug {slug} --base-dir ./masters
python tools/skill_writer.py \
  --action create \
  --slug {slug} \
  --name "{name}" \
  --base-dir ./masters \
  --meta meta.json \
  --persona persona.md \
  --memory mentor_memory.md
```

---

## 更新模式

### 追加材料

用户给新聊天、新截图、新描述时：

1. 读取新材料
2. 读取旧的 `persona.md` 和 `mentor_memory.md`
3. 参考 `prompts/merger.md` 做增量合并
4. 备份旧版本
5. 重建 `SKILL.md`

### 纠正人设

用户说“这不像他”“他不会这么说”时：

1. 参考 `prompts/correction_handler.md`
2. 判断是 `Persona` 还是 `Mentor Memory` 的问题
3. 写入 correction
4. 重建最终 Skill

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

## 要求

这个 skill 不要做复杂设定。

你就把它当成：

- `同事.skill` 的工作流
- `燕云师父` 的人物对象
- `聊天记录 + 主观描述` 的输入
- `Mentor Memory + Persona` 的输出

只要最后生成出来的东西像“这个师父本人”，而不是像一个会讲燕云的 AI，就算成功。
