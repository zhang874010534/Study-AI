from datetime import datetime

from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder, AIMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
prompt = PromptTemplate.from_template("讲一个关于{subject}的笑话")

print(prompt.format(subject="程序员"))
prompt_value = prompt.invoke({"subject": "程序员"})
print(prompt_value.to_string())
print(prompt_value.to_messages())

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个聊天机器人,当前时间为{now}"),
    MessagesPlaceholder('chat_history'),
    HumanMessagePromptTemplate.from_template("讲一个关于{subject}的笑话")
]).partial(now=datetime.now())

chat_prompt_value = chat_prompt.invoke({
    # "now": datetime.now(),
    "chat_history": [
        HumanMessage("你是什么模型"),
        AIMessage("我是 GPT-5.6 Sol")
    ],
    "subject": "程序员",
})

print(chat_prompt_value)
print(chat_prompt_value.to_string())
