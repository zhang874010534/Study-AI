import os
from typing import Any

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
dotenv.load_dotenv()


prompt = ChatPromptTemplate.from_template("{query}")

llm = ChatOpenAI(
    model="ep-20260827220313-29tvz",
    api_key=os.getenv("ARK_API_KEY"),
    base_url="https://ark.cn-beijing.volces.com/api/v3"
)

parser = StrOutputParser()

class Chain:
    steps: list = []
    def __init__(self, steps: list):
        self.steps = steps

    def invoke(self, input: Any) -> Any:
        for step in self.steps:
            input = step.invoke(input)
            print(f"step: {step}")
            print(f"input: {input}")
        return input

chain = Chain([prompt, llm, parser])
chain.invoke({"query": "你好"})
