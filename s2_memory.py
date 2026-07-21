from dotenv import load_dotenv; load_dotenv()                      # 1. 读取 .env 文件中的 API 密钥
from openrouter import OpenRouter                                  # 2. 导入 OpenRouter SDK
import os                                                          # 3. 用于读取环境变量

with OpenRouter(                                                   # 4. 创建客户端
    api_key=os.getenv("OPENROUTER_API_KEY")
) as client:
    messages = []                                                  # 5. 对话历史（关键！这就是"记忆"）
    while True:                                                    # 6. 无限循环 = 持续对话
        user_input = input("\n你：")                                # 7. 等待用户输入
        messages.append({"role": "user", "content": user_input})   # 8. 把用户消息存入历史
        response = client.chat.send(                               # 9. 发送完整对话历史给 AI
            model="anthropic/claude-opus-4.6",                     # 10. 选择模型
            messages=messages                                      # 11. 传入全部历史，而非单条消息
        )
        reply = response.choices[0].message.content                # 12. 提取 AI 回复
        messages.append({"role": "assistant", "content": reply})   # 13. 把 AI 回复也存入历史
        print(reply)                                               # 14. 打印 AI 的回复
# MIT License | 郑先隽，北师大心理学部教授，人本AI设计与创新
