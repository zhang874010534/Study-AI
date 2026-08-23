from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("""
你正在模拟{person}

下面是一个交互例子

Q: {example_q}
A: {example_a}

请根据以上描述和交互例子，回答用户的问题

Q: {input}
A:
""")

result = prompt.format(
    person="李白",
    example_q="你喜欢什么？",
    example_a="我喜爱饮酒作诗。",
    input="你觉得月亮怎么样？"
)
print(result)
