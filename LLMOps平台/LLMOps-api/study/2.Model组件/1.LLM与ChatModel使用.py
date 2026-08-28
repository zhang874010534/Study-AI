import os

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from datetime import datetime
from openai import OpenAI
from langchain_openai import ChatOpenAI
dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "回答用户的问题,现在的时间是{now}"),
    ("human", "{query}"),
]).partial(now=datetime.now())

api_key = os.getenv("ARK_API_KEY")
llm = ChatOpenAI(
    model="ep-20260827220313-29tvz",
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    api_key=api_key,
)
