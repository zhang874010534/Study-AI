from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("讲一个关于{subject}的笑话") + '，请用{language}回答'

print(prompt.invoke(subject="程序员", language="中文"))
