from ast import For


dict = [
    {'name': '张三', 'age': 18, 'isLeader': True, 'salary': 1000},
    {'name': '李四', 'age': 19, 'isLeader': False, 'salary': 0},
    {'name': '王五', 'age': 20, 'isLeader': False, 'salary': 0}
]
print(dict[0]['name'])
for item in dict:
    if item['isLeader']:
        item['salary'] += 1000
print(dict)

# f""：表示这是一个 f-string，Python 会自动解析大括号{}内的表达式
# {1:03d}：这是格式化的核心部分，格式为{值:格式说明符}
# 1：要格式化的原始数字
# :：分隔符，左边是要格式化的值，右边是格式规则
# 0：表示不足位数时用 0 填充（如果不写 0，默认用空格填充）
# 3：表示格式化后的总宽度为 3 个字符
# d：表示将值格式化为十进制整数
print(f"{1:03d}")