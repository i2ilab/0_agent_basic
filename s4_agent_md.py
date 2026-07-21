from dotenv import load_dotenv; load_dotenv()                                                        # 1. 读取 .env 文件中的 API 密钥
from openrouter import OpenRouter                                                                    # 2. 导入 OpenRouter SDK
import os                                                                                            # 3. 用于读取环境变量和执行命令
with OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY")) as client:                                  # 4. 创建客户端
    messages = [{"role":"system","content":open("agent.md").read()}]                                  # 5. 从文件读取系统提示词
    while True:                                                                                      # 6. 外层循环：等待用户新任务
        user_input = input("\n你：")                                                                  # 7. 等待用户输入
        messages.append({"role":"user","content":user_input})                                        # 8. 存入对话历史
        while True:                                                                                  # 9. 内层循环：Agent 自主执行
            response = client.chat.send(model="anthropic/claude-opus-4.6",messages=messages)          # 10. 调用 AI
            reply = response.choices[0].message.content                                              # 11. 提取 AI 回复
            messages.append({"role":"assistant","content":reply})                                     # 12. 存入历史
            if reply.strip().startswith("完成:"):                                                     # 13. AI 说"完成" → 跳出
                break
            command = reply.strip().split("命令:")[1].strip()                                         # 14. 提取命令
            result = os.popen(command).read()                                                        # 15. 执行命令
            messages.append({"role":"user","content":f"执行完毕:{result}"})                            # 16. 结果反馈给 AI
# MIT License | 郑先隽，北师大心理学部教授，人本AI设计与创新
