# -*- coding: utf-8 -*-
"""0_agent_basic 模块导览 deck —— Fathom 数据叙事风 (Path A, html2pptx 原生可编辑).
画布 960x540px. 与 lecture/v2.0 数据叙事风、1_DEFINE_guide slides 同源。"""
import os

BG="#FFFFFF"; INK="#2B2B2B"; NAVY="#1A365D"; ACC="#C2410C"
GREEN="#2D7D46"; RED="#B03A2E"; GREY="#8A8A8A"; LINE="#E3E1DC"
PANEL="#F6F4EF"; NAVYT="#EAF0F6"
FCJK="'PingFang SC','Helvetica Neue',sans-serif"
FNUM="'Helvetica Neue','PingFang SC',Arial,sans-serif"
W,H=960,540; MX=56; CW=W-2*MX

def rect(x,y,w,h,fill=None,border=None,bw=1.5,radius=0):
    s=f"position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;box-sizing:border-box;"
    if fill:s+=f"background:{fill};"
    if border:s+=f"border:{bw}px solid {border};"
    if radius:s+=f"border-radius:{radius}px;"
    return f'<div style="{s}"></div>'
def hline(x,y,w,color=NAVY,h=2): return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color};"></div>'
def vline(x,y,h,color=NAVY,w=2): return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{color};"></div>'
def txt(x,y,w,s,size=17,color=INK,weight=400,align="left",lh=1.35,tag="p",font=FCJK,ls="0px"):
    st=(f"position:absolute;left:{x}px;top:{y}px;width:{w}px;margin:0;padding:0;"
        f"font-family:{font};font-size:{size}px;color:{color};font-weight:{weight};"
        f"text-align:{align};line-height:{lh};letter-spacing:{ls};")
    return f'<{tag} style="{st}">{s}</{tag}>'
def bullets(x,y,w,items,size=15,color=INK,lh=1.6,gap=4):
    lis="".join(f'<li style="margin:0 0 {gap}px 0;padding:0;">{it}</li>' for it in items)
    st=(f"position:absolute;left:{x}px;top:{y}px;width:{w}px;margin:0;padding:0 0 0 18px;"
        f"font-family:{FCJK};font-size:{size}px;color:{color};line-height:{lh};list-style:disc;")
    return f'<ul style="{st}">{lis}</ul>'
def kicker(k): return txt(MX,38,CW,k.upper(),12,NAVY,700,ls="1.5px")
def title(t,y=60,size=32,color=INK): return txt(MX,y,CW,t,size,color,700,lh=1.18)
def rule(y,x=MX,w=54): return hline(x,y,w,ACC,3)
def foot(deck,page): return [txt(MX,512,460,deck,11,GREY,500),txt(W-140,512,84,f"{page:02d}",11,GREY,600,align="right",font=FNUM)]
def source(s,y=508,x=MX): return txt(x,y,CW,s,11,GREY,400,lh=1.3)
def page(bl):
    body=("<body style='margin:0;padding:0;width:960px;height:540px;position:relative;"
          f"background:{BG};overflow:hidden;'>"+"".join(bl)+"</body>")
    return ("<!doctype html><html><head><meta charset='utf-8'>"
            "<style>*{box-sizing:border-box;}p,h1,h2,h3,h4,ul,li{margin:0;}</style></head>"+body+"</html>")

def cards(items,y,h,accents=None,gap=18,top=18,bodysize=13):
    n=len(items); cw=(CW-gap*(n-1))//n; b=[]
    for i,(lab,tt,bd) in enumerate(items):
        x=MX+i*(cw+gap); acc=accents[i] if accents else NAVY
        b.append(rect(x,y,cw,h,fill="#FFFFFF",border=LINE,bw=1.4)); b.append(vline(x,y,h,acc,4))
        if lab: b.append(txt(x+16,y+top,cw-26,lab.upper(),11,acc,700,ls="1px"))
        b.append(txt(x+16,y+top+(20 if lab else 0),cw-26,tt,16,INK,700,lh=1.22))
        b.append(txt(x+16,y+top+(48 if lab else 26),cw-26,bd,bodysize,INK,400,lh=1.5))
    return b

FMONO="'Menlo','Courier New',monospace"
DECK="0_agent_basic · 从零打造一个 AI 智能体"; P=[]

def stagepage(pg,kick,tt,codelines,expl,prod,mind,note,emph=False):
    """s0–s7 阶段页模板:左=关键代码+讲解, 右=产品对照/认知对照, 底=思考题或痛点."""
    acc=ACC if emph else NAVY
    b=[kicker(kick),title(tt),rule(112)]
    b+=[rect(MX,178,516,232,fill=("#FBF1EC" if emph else "#FFFFFF"),border=(ACC if emph else LINE),bw=(1.8 if emph else 1.4)),
        vline(MX,178,232,acc,5),
        txt(MX+22,194,470,"关键代码",12,acc,700,ls="1px")]
    for i,cl in enumerate(codelines):
        b.append(txt(MX+22,220+i*21,474,cl,12.5,NAVY,600,font=FMONO,lh=1.3))
    b.append(bullets(MX+22,224+len(codelines)*21+8,468,expl,13.5,lh=1.6))
    x2=MX+532; wr=CW-532
    b+=[rect(x2,178,wr,110,fill=NAVYT,border=LINE,bw=1.2),
        txt(x2+16,192,wr-30,"🔗 产品对照",12,NAVY,700,ls="1px"),
        txt(x2+16,216,wr-30,prod,12.5,INK,400,lh=1.5),
        rect(x2,300,wr,110,fill=PANEL,border=LINE,bw=1.2),
        txt(x2+16,314,wr-30,"🧠 认知对照",12,NAVY,700,ls="1px"),
        txt(x2+16,338,wr-30,mind,12.5,INK,400,lh=1.5)]
    b.append(txt(MX,432,CW,note,13,GREY,500,lh=1.4))
    b+=foot(DECK,pg); return page(b)

# ── 01 封面 ──
P.append(page([
    rect(0,0,W,6,fill=NAVY),
    txt(MX,120,CW,"0_agent_basic",52,NAVY,800,font=FNUM,lh=1.0),
    rule(196,MX,72),
    txt(MX,216,CW,"从零打造一个 AI 智能体",34,INK,800,lh=1.2),
    txt(MX,278,CW,"s0 → s7 · 造得出来,才算真懂",18,GREY,500),
    txt(MX,340,CW,"WHAT I CAN'T CREATE, I DON'T UNDERSTAND",12,NAVY,700,ls="2px"),
    txt(MX,470,CW,"《AI智能体在心理与教育的应用》· 北京师范大学心理学部",13,GREY,400),
]))
# ── 02 定位 ──
b=[kicker("定位 · 从「会聊天」到「会干活」"),title("Agent = LLM + Harness"),rule(112)]
b+=cards([("LLM","大脑:会理解、会决策","语言模型负责「想」——但它本身只能输出文字,说得再好也做不了事"),
          ("HARNESS","身体:循环·记忆·工具","一圈代码把 LLM 接上现实:能连续听、记得住、动得了手"),
          ("本模块","八步亲手造出来","s0 → s7,每步只加几行代码,长成一个会倾听、会写评语的心理/教育 agent")],
         178,196,accents=[NAVY,ACC,NAVY])
b.append(txt(MX,404,CW,"你已经指挥过 Claude Code 干活;这个模块,你亲手造出它内核的最小版本。",13,GREY,500))
b+=foot(DECK,2); P.append(page(b))
# ── 03 一条主线八个阶段 ──
b=[kicker("主线 · S0 → S7"),title("八个阶段,每步只加一个想法"),rule(112)]
stages=[("s0","一次调用"),("s1","多轮对话"),("s2","对话记忆"),("s3","Agent 核心"),
        ("s4","提示词分离"),("s5","可插拔技能"),("s6","领域 Agent"),("s7","多技能协同")]
cw=(CW-7*8)//8
for i,(sid,lab) in enumerate(stages):
    x=MX+i*(cw+8); y=170; em=(i==3)
    b.append(rect(x,y,cw,96,fill=("#FBF1EC" if em else "#FFFFFF"),border=(ACC if em else LINE),bw=(2 if em else 1.3)))
    b.append(txt(x,y+14,cw,sid,22,(ACC if em else NAVY),800,align="center",font=FNUM))
    b.append(txt(x+4,y+52,cw-8,lab,11.5,INK,600,align="center",lh=1.25))
seg=(CW-24)//3
b+=[rect(MX,290,seg,64,fill=NAVYT,border=LINE,bw=1.2),
    txt(MX+14,302,seg-28,"s0–s2 · 理解 LLM",13,NAVY,800),
    txt(MX+14,324,seg-28,"它只会预测下一句,记忆全靠我们端给它",11.5,GREY,500),
    rect(MX+seg+12,290,seg,64,fill="#FBF1EC",border=ACC,bw=1.5),
    txt(MX+seg+26,302,seg-28,"s3–s4 · 装上手和规则",13,ACC,800),
    txt(MX+seg+26,324,seg-28,"从聊天变成会干活的 agent",11.5,GREY,500),
    rect(MX+2*seg+24,290,seg,64,fill=NAVYT,border=LINE,bw=1.2),
    txt(MX+2*seg+38,302,seg-28,"s5–s7 · 注入专业",13,NAVY,800),
    txt(MX+2*seg+38,324,seg-28,"技能文件把「心理咨询」变成能力",11.5,GREY,500)]
b.append(txt(MX,384,CW,"s3 是分水岭:在它之前,agent 只会「说」;从它开始,agent 会「做」。",13,GREY,500))
b+=foot(DECK,3); P.append(page(b))
# ── 04 s0 一次调用 ──
P.append(stagepage(4,"S0 · 一次调用","和 AI 说一句、收一句,这就是一切的起点",
    ['client.chat.send(model=..., ','    messages=[{"role":"user","content":"你好"}])'],
    ["发一条 user 消息,打印一条回复,程序结束","messages 列表——之后一切都长在它上面"],
    "你在网页上问一句 ChatGPT、它答一句——本质就是这段代码。",
    "像膝跳反射:给刺激出反应,做完就忘——一次性的反射。",
    "思考题:s0 只能问一次。想让它「接着聊」,要加什么?(→ s1)"))
# ── 05 s1 多轮对话 ──
P.append(stagepage(5,"S1 · 多轮对话","能连续聊,但记不住任何事",
    ['while True:','    user_input = input("\\n你：")'],
    ["「我压力很大 → 那我该怎么办?」——「那」指什么,它不知道","每次只把当前这句发给 AI;辅导/咨询里这是致命的"],
    "ChatGPT 网页版的多轮框——但不带历史,就是这个「健忘版」。",
    "跟一个每句话说完就失忆的人聊天——健忘的对话者。",
    "思考题:s1 每次发给 AI 的,是「全部历史」还是「就这一句」?(对比 s2)"))
# ── 06 s2 对话记忆 ──
P.append(stagepage(6,"S2 · 对话记忆","ChatGPT「记住上文」的机制,就这 3 行",
    ['messages = []','messages.append({"role":"user", ...})','messages.append({"role":"assistant", ...})'],
    ["每次把全部历史一起发过去,AI 就「记住」了","聊了几轮再问「结合我一开始说的给点建议」,它还记得日记细节"],
    "ChatGPT 记住上文,靠的就是每次把之前对话一起发过去。",
    "工作记忆——把说过的话「端在手上」,才能接着想。",
    "思考题:删掉「记录 AI 回复」那一次 append,会怎样?试试再跑。"))
# ── 07 s3 Agent 核心(分水岭) ──
P.append(stagepage(7,"S3 · AGENT 核心 —— 分水岭","从「只会说」到「会动手」:双层循环 + 执行命令",
    ['while True:            # 外层:等用户任务','    while True:        # 内层:自主执行到「完成:」','        result = os.popen(command).read()'],
    ["「读作文目录,告诉我哪篇更需要修改」——它自己 ls → 逐篇 cat → 比较,连跑好几轮","聊天机器人做不到:感知 → 决策 → 行动 → 再感知"],
    "你指挥过的 Claude Code,内核就是这个双层循环。",
    "从「想」到「做」——第一次能行动:感知→决策→行动→再感知。",
    "思考题:内层循环不等你输入、自己往前跑,它靠什么判断「做完了」?(看「完成:」)",emph=True))
# ── 08 s4 提示词分离 ──
P.append(stagepage(8,"S4 · 提示词分离","改行为,不用改代码",
    ['messages = [{"role":"system",','    "content": open("agent.md").read()}]'],
    ["写死的规则搬进 agent.md","加一句「执行前先说『收到』」重跑——一行 Python 没动,行为就变了"],
    "ChatGPT 的「自定义指令」、各家产品的 system prompt。",
    "指令与执行分离——换「岗位说明书」就换做法,不用换人。",
    "思考题:想给 AI 加一整套「专业知识」,该怎么做?(→ s5)"))
# ── 09 s5 可插拔技能 ──
P.append(stagepage(9,"S5 · 可插拔技能","换技能 = 换专家:GPTs 的本质",
    ['prompt = open("agent.md").read() \\','       + open("skill.md").read()'],
    ["agent.md 管「怎么做」,skill.md 管「做什么领域」","换成 skill_feedback.md:按「3 优点 + 1 改进 + 鼓励」评作文,从泛泛变专家"],
    "你在 ChatGPT 里建的 GPTs / 自定义 GPT,本质就是这一行拼接。",
    "专业知识载入——读了「CBT 手册」就会做 CBT。",
    "思考题:只换 skill 文件、代码一行不改,这个 agent 还能变成什么专家?"))
# ── 10 s6 领域 Agent ──
P.append(stagepage(10,"S6 · 领域 AGENT","决定它是谁的,不是代码,是技能文件",
    ['prompt = open("agent.md").read() \\','       + open("skill_tutor.md").read()'],
    ["代码和 s5 一字不差,只换加载的 skill 文件","skill_tutor = 课程导师,skill_feedback = 作文老师——同一份代码,判若两人"],
    "你收藏的不同 GPTs:底层同一个模型,区别只在那份说明。",
    "换个角色/人设——穿老师的衣服是老师,穿教练的衣服是教练。",
    "思考题:s5 和 s6 代码几乎一样,为什么还分成两个文件讲?它想让你记住什么?"))
# ── 11 s7 多技能协同 ──
P.append(stagepage(11,"S7 · 多技能协同","倾听 + CBT,融进同一次回应",
    ['skills = ["skill_listen.md", "skill_cbt.md"]','prompt = open("agent.md").read() \\','       + "".join(open(s).read() for s in skills)'],
    ["读心情日记:先温暖倾听「写出来已经很勇敢」,再温和引导「我天生就笨」这种以偏概全","单技能做不到这种融合——只比 s5 多一行"],
    "复合 GPT / 工作流:多个技能组合成一种能力。",
    "成熟咨询师既会倾听,又会在合适时机做认知引导。",
    "思考题:s7 只多一行。「给 agent 加能力」,难在写代码,还是难在写好技能?"))
# ── 12 核心公式(大字) ──
b=[rect(0,0,W,H,fill=NAVY),
   txt(MX,86,CW,"核心公式 · THE FORMULA",14,"#8FB0CC",800,ls="3px",font=FNUM),rule(126,MX,72),
   txt(MX,152,CW,"Agent = LLM + 循环 + 记忆 + 工具 + 技能",30,"#FFFFFF",800,lh=1.25)]
terms=[("LLM","s0 · 会说"),("循环","s1 · 会连续"),("记忆","s2 · 记得住"),("工具","s3 · 会动手"),("技能","s5–s7 · 懂专业")]
cw=(CW-4*14)//5
for i,(t,d) in enumerate(terms):
    x=MX+i*(cw+14); y=230
    b.append(rect(x,y,cw,92,fill="#24466B",border="#3A5B80",bw=1.2))
    b.append(txt(x,y+18,cw,t,22,"#FFFFFF",800,align="center"))
    b.append(txt(x,y+54,cw,d,12,"#8FB0CC",600,align="center",font=FNUM))
b+=[txt(MX,368,CW,"Agent = LLM + 循环 + 工具调用(s3)",15,"#C6D6E6",600,font=FMONO),
    txt(MX,396,CW,"领域 Agent = Agent + Skill(s5 · s6)",15,"#C6D6E6",600,font=FMONO),
    txt(MX,424,CW,"多能 Agent = Agent + [Skill, Skill…](s7)",15,"#C6D6E6",600,font=FMONO),
    txt(MX,478,CW,"带走这三行——你造的每一个 agent,都是这条公式的一次展开。",13,"#8FB0CC",400)]
P.append(page(b))
# ── 13 demo_workspace ──
b=[kicker("练习靶子 · DEMO_WORKSPACE"),title("机制的价值,只有在真实场景里才看得出来"),rule(112)]
b+=cards([("作文批改","两篇学生作文","「给小明的作文写评语」——技能让评语从泛泛变专业"),
          ("心情日记","一位初三学生的困扰","「有点撑不住」——倾听 + CBT 的组合在这里显出价值"),
          ("待办清单","助教的真实活儿","「把作文按主题分类」——agent 自己规划、动手完成")],
         178,196,accents=[NAVY,ACC,NAVY])
b.append(txt(MX,404,CW,"一个模拟「心理/教育助教工作台」的沙盒:每个阶段的复杂例子和作业都在它上面跑——简单任务用不上,真实工作离不开。",13,GREY,500,lh=1.4))
b+=foot(DECK,13); P.append(page(b))
# ── 14 作业1 ──
b=[kicker("作业 1 · HOMEWORK"),title("费曼自测 + 扩展三选一"),rule(112)]
b+=[rect(MX,178,(CW-24)//2,232,fill=NAVYT,border=NAVY,bw=1.6),
    txt(MX+20,196,360,"A · 费曼重写 s2(必做)",15,NAVY,800),
    bullets(MX+20,230,(CW-24)//2-44,["盖住原文,凭理解默写 s2_memory.py","跑通「我叫小明 → 我叫什么」记忆测试","卡住的那一行,就是你其实还没真懂的地方"],14,lh=1.7)]
x2=MX+(CW-24)//2+24
b+=[rect(x2,178,(CW-24)//2,232,fill="#FFFFFF",border=ACC,bw=1.6),
    txt(x2+20,196,360,"B · 三选一(必做)",15,ACC,800),
    bullets(x2+20,230,(CW-24)//2-44,["① 写你自己的作文反馈技能(苏格拉底式/结构诊断式…)","② 打磨 s7 的倾听 + CBT 组合,回应心情日记","③ 给 s3 布置任务:作文按主题分类,生成 分类.md"],14,lh=1.7)]
b.append(txt(MX,428,CW,"Capstone 加分:让你的 agent 当一次完整的「老师」——一篇作文一份评语,再答:它像不像真老师,差在哪?",13,GREY,500))
b+=foot(DECK,14); P.append(page(b))
# ── 15 AI 教练 ──
b=[kicker("AI 教练 · COACH SKILLS"),title("两个教练带着走:陪跑,不代写"),rule(112)]
b+=cards([("/AGENT-TUTOR","概念陪跑 · 费曼式","一个阶段一个阶段问你「讲给我听」——讲不出的地方,就是没真懂的地方"),
          ("/AGENT-HW1","作业陪跑 · 三级提示","概念级 → 操作级 → 兜底级,一层层翻;只指路,绝不替你写答案"),
          ("三条路径","可混用","网页版 web/index.html 可视化 · 教程 + 逐个跑代码 · 让教练带着走")],
         178,196,accents=[NAVY,ACC,NAVY])
b.append(txt(MX,404,CW,"问概念、问报错、问怎么写某个小功能——都行;让 AI 把整道题的答案写给你——不行。你交的每一行,都要能自己解释。",13,GREY,500,lh=1.4))
b+=foot(DECK,15); P.append(page(b))
# ── 16 i2i Academy ──
b=[kicker("平台 · I2I ACADEMY"),title("浏览器里零安装,跑完 s0 → s7"),rule(112)]
b.append(txt(MX,124,CW,"课程原版 .py 逐字节不改,在浏览器里就能跑通完整 agent 循环——没配好本地环境,也不耽误学。",14,GREY,500))
b+=cards([("零安装","Pyodide 直接跑","编辑器 + 终端 + stdin 输入框,input() 与 chat.send() 原样工作"),
          ("判题门禁","过了才解锁下一关","每个阶段自动判题,亲手跑通才算学会"),
          ("MOCK / REAL","双模式","mock 按脚本回复、零 token 自动判题;real 连真模型实战")],
         196,186,accents=[NAVY,ACC,NAVY])
b.append(txt(MX,400,CW,"平台内容直读课程仓库构建(hash 锁),与你手里的代码永不漂移。",13,GREY,500))
b+=foot(DECK,16); P.append(page(b))
# ── 17 安全与诚信 ──
b=[kicker("红线 · SAFETY & INTEGRITY"),title("能力越大,越要先立规矩"),rule(112)]
b+=cards([("安全提示词","agent_safe.md","识别自伤/自杀意念 → 立即给心理援助热线,不做诊断、不开处方"),
          ("密钥安全",".env 绝不提交","API key 只放 .env,.gitignore 挡住它——一次泄漏,全网可用"),
          ("心理红线","危机转介真人","极端情绪 → 建议求助老师/热线;AI 是教学演示,不是专业心理服务"),
          ("学术诚信","代码自己敲","问概念可以,AI 代写整题不行;每一行你都要能对助教讲清")],
         178,208,accents=[NAVY,NAVY,RED,ACC],bodysize=12.5)
b.append(txt(MX,416,CW,"在心理与教育场景,这些不是「附加项」——是从第一行代码就要守住的底线。",13,GREY,500))
b+=foot(DECK,17); P.append(page(b))
# ── 18 模块地图 ──
b=[kicker("模块地图 · WHERE NEXT"),title("造行为 → 造框架 → 定义 → 上线"),rule(112)]
mods=[("0","造行为","0_agent_basic:s0–s7,亲手造出会干活的 agent",True),
      ("1","造框架","1_claude_code_basic:c0–c5,复现 mini Claude Code",False),
      ("2","定义与评估","DEFINE 双支柱:想清楚造什么、凭什么说它行",False),
      ("3","上线","Build & Ship:前后端连通,部署上公网",False)]
cw=(CW-3*14)//4
for i,(num,name,desc,em) in enumerate(mods):
    x=MX+i*(cw+14); y=178
    b.append(rect(x,y,cw,150,fill=("#FBF1EC" if em else "#FFFFFF"),border=(ACC if em else LINE),bw=(2 if em else 1.4)))
    b.append(txt(x+14,y+14,cw-24,num,26,(ACC if em else NAVY),800,font=FNUM))
    b.append(txt(x+14,y+52,cw-24,name,15,INK,700))
    b.append(txt(x+14,y+78,cw-26,desc,11.5,GREY if not em else INK,400,lh=1.45))
    if i<3: b.append(txt(x+cw-3,y+58,18,"→",18,ACC,800))
b.append(txt(MX,356,CW,"本模块给你「造行为」的手;下一步,把这双手升级成一整套工业级框架。",13,GREY,500))
b+=foot(DECK,18); P.append(page(b))
# ── 19 结课 ──
P.append(page([rect(0,0,W,6,fill=NAVY),
    txt(MX,130,CW,"带走一句话",13,NAVY,700,ls="2px"),rule(166,MX,72),
    txt(MX,196,CW-40,"「造得出来,才算真懂。」",40,INK,800,lh=1.3),
    txt(MX,268,CW-40,"八段代码,每段几行——",26,GREY,600,lh=1.4),
    txt(MX,310,CW-40,"但你亲手造出了一个会干活的智能体。",26,ACC,800,lh=1.4),
    txt(MX,392,CW,"下一站:把它长成你自己的 mini Claude Code。",15,GREY,500),
    txt(MX,470,CW,"郑先隽 · 北京师范大学心理学部 · 人本 AI 设计与创新",13,GREY,400)]))

HERE=os.path.dirname(os.path.abspath(__file__))
d=os.path.join(HERE,"html"); os.makedirs(d,exist_ok=True)
for i,html in enumerate(P,1):
    open(os.path.join(d,f"{i:02d}.html"),"w",encoding="utf-8").write(html)
print(f"{len(P)} pages")
