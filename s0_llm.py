from dotenv import load_dotenv; load_dotenv()                      # 1. 读取 .env 文件中的 API 密钥
from openrouter import OpenRouter                                  # 2. 导入 OpenRouter SDK
import os                                                          # 3. 用于读取环境变量

client = OpenRouter(api_key=os.getenv("OPENROUTER_API_KEY"))       # 4. 创建客户端
response = client.chat.send(                                       # 5. 发送聊天请求
    model="anthropic/claude-opus-4.6",                             # 6. 选择模型
    messages=[                                                     # 7. 消息列表（对话历史）
        {"role": "user", "content": "你好"}                         # 8. 一条用户消息
    ]
)
print(response.choices[0].message.content)                         # 9. 打印 AI 的回复
# MIT License | 郑先隽，北师大心理学部教授，人本AI设计与创新
