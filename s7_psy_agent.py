from dotenv import load_dotenv; load_dotenv()                      # 1. 读取 .env 文件中的 API 密钥
from openrouter import OpenRouter                                  # 2. 导入 OpenRouter SDK
import os                                                          # 3. 用于读取环境变量和执行命令

with OpenRouter(                                                   # 4. 创建客户端
    api_key=os.getenv("OPENROUTER_API_KEY")
) as client:
    skills = ["skill_listen.md", "skill_cbt.md"]                   # 5. 多个技能文件：倾听 + CBT
    prompt = open("agent.md").read() + "".join(open(s).read() for s in skills)  # 6. 拼接：通用提示词 + 所有技能
    messages = [{"role":"system","content":prompt}]                 # 7. 系统提示词 = agent.md + 多个 skill

    while True:                                                    # 8. 外层循环：等待用户输入新任务
        user_input = input("\n你：")                                # 9. 等待用户输入
        messages.append({"role": "user", "content": user_input})   # 10. 存入对话历史

        while True:                                                # 11. 内层循环：Agent 自主执行，直到任务完成
            response = client.chat.send(                           # 12. 发送对话历史给 AI
                model="anthropic/claude-opus-4.6",
                messages=messages
            )
            reply = response.choices[0].message.content            # 13. 提取 AI 回复
            messages.append({"role": "assistant", "content": reply})# 14. 存入历史
            print(f"[AI] {reply}")                                 # 15. 打印 AI 的决策

            if reply.strip().startswith("完成:"):                   # 16. 如果 AI 说"完成" → 跳出内层循环
                break

            command = reply.strip().split("命令:")[1].strip()       # 17. 提取 AI 想执行的命令
            result = os.popen(command).read()                      # 18. 执行命令（如记录情绪/思维）
            print(f"[系统] {result}")                               # 19. 打印命令结果
            messages.append({"role": "user", "content": f"执行完毕:{result}"})  # 20. 把结果反馈给 AI
# MIT License | 郑先隽，北师大心理学部教授，人本AI设计与创新
