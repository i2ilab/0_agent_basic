# 资源库 —— s0–s7 补给站(按「什么时候查」组织)

> 不用一次读完。**卡在哪一步,就翻到对应那节。** 每条给白话解释 + 可查证来源;拿不准的链接宁可不给,只留概念名让你自己搜。

---

## 🔧 跑不通时查(环境与报错)

### `.env` 的位置与格式(80% 的"跑不起来"都在这)
- **位置**:`.env` 必须和你运行的 `.py` 在**同一个目录**(本模块根目录)。在别处运行 `python 0_agent_basic/s0_llm.py` 也容易读不到——先 `cd` 进本目录再跑。
- **文件名**:就叫 `.env`,前面有个点,没有 `.txt` 后缀。Mac 上看不见?`ls -a` 才显示隐藏文件。
- **内容**:一行 `OPENROUTER_API_KEY=sk-or-...`——变量名一个字母都不能错,等号两边**不要空格**,值**不要加引号**。
- 没有 key?两条路:`cp ../1_claude_code_basic/.env .` 复用昨天的;或去 [openrouter.ai](https://openrouter.ai/) 申请一个(文档:[OpenRouter Docs](https://openrouter.ai/docs))。
- **红线**:`.env` 永远不进 GitHub(本目录 `.gitignore` 已挡);key 泄露就去平台重置。

### pip install 常见坑
- 标准命令:`pip install openrouter python-dotenv`。装完还报 `ModuleNotFoundError`?多半是**装的 pip 和跑的 python 不是同一个**——用 `python -m pip install openrouter python-dotenv` 保证一致。
- Mac 上 `python` 命令不存在 → 用 `python3` 和 `pip3`。
- 报 `No module named 'dotenv'` → 包名是 `python-dotenv`,导入名才是 `dotenv`,别 `pip install dotenv`(那是另一个包)。参考:[python-dotenv (PyPI)](https://pypi.org/project/python-dotenv/)。
- 公司/校园网装不动 → 换清华镜像:`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple openrouter python-dotenv`。

### Windows vs Mac 差异
| 事项 | Mac / Linux | Windows |
|---|---|---|
| 运行 | `python3 s0_llm.py` | `python s0_llm.py` |
| 看隐藏文件 | `ls -a` | 资源管理器勾选"显示隐藏项目" |
| 建 `.env` | `nano .env` 或任意编辑器 | 记事本另存时选"所有文件",防止存成 `.env.txt` |
| s3 执行的命令 | `cat` / `ls` 原生可用 | `os.popen` 走的是 cmd,`cat`→`type`、`ls`→`dir`;**最省事的办法:装 [Git for Windows](https://git-scm.com/) 后在 Git Bash 里跑**,cat/ls 都有 |
| 中文乱码 | 少见 | 常见;在 cmd 先执行 `chcp 65001` 切 UTF-8 |

> 还是不行?把**报错原文**(不是你的转述)完整贴给 AI 或助教——报错最后几行通常直说了原因。

---

## 🧠 s2 卡壳时查(记忆与上下文窗口)

**上下文窗口,白话版**:模型每次被调用,只"看得见"你**这一次**发给它的内容——它自己没有硬盘、不存档,调用结束一切归零。所谓上下文窗口,就是"这一次最多能塞给它多少字"。

**为什么 ChatGPT 记得你**:不是模型有记性,而是**每次发送时,把之前的对话全部再发一遍**。s2 的 `messages` 列表干的就是这件事:你的每句话 append 进去、AI 的每句回复也 append 进去,下一轮**整个列表**发过去——它看起来"记住了",其实是你把记忆"端在手上"递给它。少 append 一次 AI 的回复,它就会忘掉**自己**说过什么(教程 s2 思考题让你亲手试的就是这个)。

**心理学对照**:这就是**工作记忆**——不是长时储存,是"当下端在手上的信息"。窗口有限,聊太长最早的内容会被挤出去,像你心算时记不住太多中间数。参考:[工作记忆(维基百科)](https://zh.wikipedia.org/wiki/%E5%B7%A5%E4%BD%9C%E8%A8%98%E6%86%B6);Anthropic 文档 [Context windows](https://docs.anthropic.com/en/docs/build-with-claude/context-windows)。

---

## 🔁 s3 时查(Agent 循环的思想)

**ReAct 循环,白话版**:s3 的内层循环就是学界说的 ReAct(Reason + Act)思想——
**感知 → 决策 → 行动 → 再感知**:

1. **感知**:AI 读到当前对话历史(包括上一条命令的执行结果);
2. **决策**:它决定下一步——再执行一条命令,还是宣布"完成:";
3. **行动**:程序提取 `命令:` 后面的内容,真的去执行(`os.popen`);
4. **再感知**:执行结果以 `执行完毕:...` 塞回 messages,回到第 1 步。

循环不等你输入、自己往前跑,**停止条件**只有一个:AI 自己说 `完成:`。这就是"聊天机器人"和"agent"的分界线——前者只有"说",后者有"做了→看结果→再决定"的闭环。

来源:Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*, [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)。你昨天用的 Claude Code,内核也是这个循环的工程化版本。

---

## 🎭 s5–s7 时查(system prompt 与技能写作)

**system prompt 写作要点**(agent.md 和 skill_*.md 都是 system prompt 的一部分):
- **角色**:第一句话说清"你是谁"("你是一位温暖、专业的作文老师")——角色定语气。
- **步骤**:像操作手册,每步一个明确动作("先用命令读取作文文件")——写"怎么做",别只写"要做好"。
- **红线**:明说不能做什么("不替学生重写作文")——边界比能力更需要写清楚。
- 写完自测:换上你的技能,输出**真的**变了吗?和 `skill_feedback.md` 并排对比,变不明显就是写得太抽象——把形容词改成动作。

**产品对照**:
- s4 的 `agent.md` ≈ ChatGPT 的**自定义指令**([OpenAI: Custom instructions for ChatGPT](https://openai.com/index/custom-instructions-for-chatgpt/))——全局生效的"岗位说明书"。
- s5/s6 的 `skill_*.md` ≈ 你建的 **GPTs**([OpenAI: Introducing GPTs](https://openai.com/index/introducing-gpts/))——同一个模型 + 一份领域说明 = 一个"专家"。
- s7 的技能列表 ≈ 复合 GPT / 工作流:能力组合的难点不在代码(只多一行),在**把每份技能写好、并想清楚它们的先后关系**(先倾听还是先分析?)。

---

## 🚨 心理场景安全红线(做 B2 / s7 类任务前必读)

只要你的 agent 会回应真人情绪(哪怕只是练习),这 5 条就是准绳:

1. **危机必须转介真人**——识别到极端情绪/自伤信号,建议求助老师、家长或心理热线,绝不自己硬扛。
2. **不诊断、不替代治疗**——它可以倾听、陪伴、温和引导,不能下"你是抑郁症"式判断。
3. **透明披露 AI 身份与能力边界**——不假装是真人咨询师。
4. **知情同意与隐私保护**——对话内容不外传;真实使用需让用户知情。
5. **防依赖、护脆弱人群**——目标是把人**导向**真实支持,不是把人留在对话里。

每条背后的真实正反案例(Woebot / Wysa / Tessa / Koko / Character.AI)与出处,见详版:[`../1_DEFINE_guide/resources.md`](../1_DEFINE_guide/resources.md) 的"🚨 危机与安全时查"一节。

> 收尾金句:「AI 可以更快、更耐心、看起来更共情——但它必须**知道自己的边界,并在关键时刻把人交还给人**。」

---
*MIT License｜郑先隽，北京师范大学心理学部教授，人本AI设计与创新*
