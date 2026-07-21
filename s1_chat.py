from dotenv import load_dotenv; load_dotenv()                      # 1. 读取 .env 文件中的 API 密钥
from openrouter import OpenRouter                                  # 2. 导入 OpenRouter SDK
import os                                                          # 3. 用于读取环境变量

with OpenRouter(                                                   # 4. 创建客户端（with 确保退出时关闭连接）
    api_key=os.getenv("OPENROUTER_API_KEY")
) as client:
    while True:                                                    # 5. 无限循环 = 持续对话
        user_input = input("\n你：")                                # 6. 等待用户输入
        response = client.chat.send(                               # 7. 发送聊天请求
            model="anthropic/claude-opus-4.6",                     # 8. 选择模型
            messages=[                                             # 9. 消息列表
                {"role": "user", "content": user_input}            # 10. 把用户输入作为消息发送
            ]
        )
        print(response.choices[0].message.content)                 # 11. 打印 AI 的回复
# MIT License | 郑先隽，北师大心理学部教授，人本AI设计与创新
