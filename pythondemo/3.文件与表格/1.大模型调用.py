import os
from volcenginesdkarkruntime import Ark
client = Ark(api_key=ARK_API_KEY)

try:
    completion = client.chat.completions.create(
    model="doubao-seed-2-0-lite-2604281",
    messages=[
        {"role": "user", "content": "分析一下下一周可以买哪些股票？"}
    ]
)
except Exception as e:
    print(e)

print(11)
print(completion.choices[0].message)