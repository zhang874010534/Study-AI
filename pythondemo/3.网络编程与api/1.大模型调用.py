import os
from volcenginesdkarkruntime import Ark
client = Ark(api_key=os.environ.get("ARK_API_KEY"))

try:
    completion = client.chat.completions.create(
        model="doubao-seed-2-0-lite-260428",
        messages=[
            {"role": "user", "content": "你好呀"}
        ]
    )
    print(completion.choices[0].message.content)
except Exception as e:
    print(e)

