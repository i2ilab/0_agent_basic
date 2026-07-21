# 0_agent_basic — 从零打造一个 AI 智能体(s0 → s7)

> 用 8 步、每步只加几行代码,从"一次 API 调用"长到一个**会倾听、会给作文写评语**的心理/教育 Agent。
> **"What I can't create, I don't understand."** —— 造得出来,才算真懂。

## 八个阶段(每步只加一个想法)

| 文件 | 新想法 | 一句话 |
|---|---|---|
| `s0_llm.py` | 一次调用 | 和 AI 说一句、收一句 |
| `s1_chat.py` | 多轮对话 | 能连续聊,但记不住 |
| `s2_memory.py` | 对话记忆 | messages 列表存历史,它就"记住"了 |
| `s3_agent.py` | Agent 核心 | 双层循环 + 执行命令,从"会说"到"会做" |
| `s4_agent_md.py` | 提示词分离 | 规则搬进 agent.md,改行为不改代码 |
| `s5_agent_skill.py` | 可插拔技能 | 换个 skill 文件 = 换个专家 |
| `s6_tutor_agent.py` | 领域 Agent | 代码不改,只换 skill |
| `s7_psy_agent.py` | 多技能 Agent | 多个技能组合成一种能力 |

## demo_workspace/ — 练习靶子(为什么要有它?)

**先说为什么给你一个"假工作台"练手。**
这些机制(记忆、工具、技能)的价值,**只有在真实场景里才看得出来**:光"问 1+1"看不出记忆有啥用,光"创建 hello.txt"看不出技能有啥用。
所以我们准备了 `demo_workspace/`——一个模拟**心理/教育助教工作台**的靶子:两篇学生作文、一段有情绪困扰的心情日记、一张待办清单。
s0–s7 的每个"复杂例子"和作业,都在这上面跑,让你亲眼看到:**同一个机制,简单任务用不上,真实工作离不开。**

```bash
cat demo_workspace/README.md
cat "demo_workspace/作文/小明_我的暑假.txt"
```

## 快速开始

```bash
# 1. 配环境(和 1_claude_code_basic / 昨天一样,复用同一个 key)
cp ../1_claude_code_basic/.env .    # 或新建 .env 写一行 OPENROUTER_API_KEY=...
pip install openrouter python-dotenv

# 2. 从 s0 开始,一个一个跑
python s0_llm.py
```

> 若单独克隆本仓库:自己建 `.env`,写入 `OPENROUTER_API_KEY=你的密钥`(去 openrouter.ai 申请)。

## 怎么学

1. **看**:浏览器打开 `web/index.html`(离线可用)——s0→s7 时间线,每阶段有"简单/复杂"两个例子、"🔗产品对照 + 🧠认知对照"两张卡、带高亮的代码、思考题。
2. **读+跑**:配套教程 `教程_从s0到心理Agent.md`,一阶段一阶段跑通。
3. **做**:作业 `作业指南_Agent作业1.md`(费曼自测 + 在 demo_workspace 上的扩展任务)。

## 技能文件说明

- `agent.md` — 通用指令(命令/完成格式)
- `skill_feedback.md` — **鼓励式作文反馈**(轻量、零依赖,s5/s6 推荐用它)
- `skill_tutor.md` — AI 课程导师
- `skill_listen.md` / `skill_cbt.md` — 心理倾听 / CBT(s7 组合用)
- `skill.md` — 视频加工(**进阶**,需装 ffmpeg/whisper,课上演示)

---
*MIT License｜郑先隽,北师大心理学部教授,人本AI设计与创新｜助教:元真、师婕*

## 🤖 AI 教练带着走

本模块自带两个 Claude Code 教练 skill——它们**只当教练、不当枪手**:提问、追问、逐级提示,不代写一行作业代码。

| skill | 什么时候用 | 一句话职责 |
|---|---|---|
| `/agent-tutor` | 学 s0–s7 时概念看不懂("双层循环什么意思""s5 和 s6 有什么区别") | 费曼式概念教练:让你讲给它听,从复述里找卡点追问 |
| `/agent-hw1` | 做作业 1 时:三选一犹豫、卡住、提交前自查 | 作业陪跑教练:帮你自己选方向,按"方向→结构→某一行"三级提示,绝不给成品 |

在本目录打开 Claude Code 输入 `/agent-tutor` 即可。配套自查表见 `checklists/学习门禁总清单.md`,卡壳补给站见 `resources.md`;助教请看 `助教_skills使用说明.md`。
