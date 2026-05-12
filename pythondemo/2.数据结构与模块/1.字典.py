lst = [1, 2, 3, 4]
people = {
    "name": "张三",
    "age": 18,
    "gender": "男"
}
# print(people.name)
print(people['name'])
print(people.get('name'))
print(people.get('name2', '默认值'))
peopleDict = dict(name = '张三', age = 18)
print(peopleDict)

people.update({'name': '李四'}) # 修改
people.update({'brother': '王五'}) # 增加
# del people['age']
# people.pop('age') # 删除键为age的元素
# people.clear() # 清空字典
people.setdefault('salary', 0) # 增加键为salary的元素，值为0
people.setdefault('salary', 1) # 增加键为salary的元素，值为1 ，如果salary已存在，则不修改
print(people)
