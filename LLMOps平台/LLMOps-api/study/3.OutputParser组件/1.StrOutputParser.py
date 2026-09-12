import os

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_template("{query}")

llm = ChatOpenAI(
    model="ep-20260827220313-29tvz",
    api_key=os.getenv("ARK_API_KEY"),
    base_url="https://ark.cn-beijing.volces.com/api/v3"
)


parser = StrOutputParser()

content = parser.invoke(
    llm.invoke(prompt.invoke({
        "query": "你好",
    }))
)

print(content)