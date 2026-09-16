import os

import dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
dotenv.load_dotenv()
# 创建一个json数据结构
class Joke(BaseModel):
    joke: str = Field(description="一个笑话")
    punchline: str = Field(description="笑话的 punchline")

parser = JsonOutputParser(pydantic_object=Joke)
# 创建一个提示模板
prompt = ChatPromptTemplate.from_template("{from_instructions}\n {query}").partial(
    from_instructions=parser.get_format_instructions(),
)

# print(prompt.format(query="请生成一个笑话"))

# 大语言模型
llm = ChatOpenAI(
    model="ep-20260827220313-29tvz",
    api_key=os.getenv("ARK_API_KEY"),
    base_url="https://ark.cn-beijing.volces.com/api/v3"
)

joke = parser.invoke(
    llm.invoke(prompt.invoke({
        "query": "请生成一个笑话",
    }))
)
print(type(joke))
print(joke.get("punchline"))
