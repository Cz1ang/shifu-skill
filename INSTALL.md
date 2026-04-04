# 安装说明

这个项目本身是一个 Skill 包，不是独立运行的服务。

你需要把它放进支持 Skill 的宿主环境里，例如：

- Codex
- Claude Code
- OpenClaw

---

## 1. Codex 安装

把仓库放到 `~/.codex/skills/` 下：

```bash
git clone <your-repo-or-local-copy> ~/.codex/skills/yysls-shifu
```

如果你现在就是本地这份目录，最直接的是把：

```text
E:\codex\yysls-shifu
```

复制到：

```text
C:\Users\你的用户名\.codex\skills\yysls-shifu
```

Windows 常见路径：

```text
C:\Users\你的用户名\.codex\skills\yysls-shifu
```

---

## 2. Claude Code 安装

### 安装到当前项目

在你的项目根目录执行：

```bash
mkdir -p .claude/skills
git clone <your-repo-or-local-copy> .claude/skills/yysls-shifu
```

如果你现在只是在本机本地使用，也可以直接复制：

```text
E:\codex\yysls-shifu
```

到：

```text
你的项目\.claude\skills\yysls-shifu
```

### 安装到全局

```bash
git clone <your-repo-or-local-copy> ~/.claude/skills/yysls-shifu
```

---

## 3. OpenClaw 安装

```bash
git clone <your-repo-or-local-copy> ~/.openclaw/workspace/skills/yysls-shifu
```

本地目录方式同样可行，直接把：

```text
E:\codex\yysls-shifu
```

复制到对应 skills 目录即可。

---

## 4. 依赖说明

这个仓库里带了两个最小脚本：

- `tools/skill_writer.py`
- `tools/version_manager.py`

理论上需要：

- Python 3.9+

当前这套实现没有额外第三方依赖。

---

## 5. 当前环境注意事项

如果你在 Windows 下使用，常见情况有两个：

1. `python` 命令可用  
   那就直接运行 README 里的命令。

2. `python` 命令不可用，但装了 Python Launcher  
   可以把命令改成：

```bash
py -3 tools/skill_writer.py --action list --base-dir ./masters
```

如果两者都不可用，就先安装 Python。

---

## 6. 创建一个新师父

在宿主环境里触发：

```text
/create-yysls-shifu
```

然后按流程提供：

- 师父称呼
- 关系描述
- 人物感觉
- 聊天记录 / 截图 / 文本 / 主观描述

---

## 7. 目录说明

### 主 Skill

- `SKILL.md`：创建器入口

### prompts

- 负责提问、分析、构建、合并、纠正

### references

- 负责材料导入规则和燕云师父类型参考

### tools

- 负责写实例、列实例、版本备份和回滚

### masters

- 存放最终生成出来的师父实例

---

## 8. Demo

仓库已自带一个示例实例：

- `masters/ajiu-shifu/`

你可以先看这个目录，理解最终产物长什么样，再替换成你自己的数据。

---

## 9. 常见问题

### Q: 没有微信/QQ导出怎么办？

可以先只靠主观描述做第一版，后续再追加材料。

### Q: 没有截图可以吗？

可以，只给文本也能做。

### Q: 结果不像他怎么办？

直接走纠正流程，说：

```text
这不对，他不会这么说
```

### Q: 想加新聊天怎么办？

直接说：

```text
追加记录
```

---

## 10. 一句话

安装完以后，这个项目就是一个“把燕云师父蒸馏成数字人格”的 Skill 创建器。
