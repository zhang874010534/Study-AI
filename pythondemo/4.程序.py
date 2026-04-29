name = '张三'
age = 18
per_salary = 200

def get_income(name, day, per_salary):
    return day * per_salary, 1
income = get_income(name, 20, per_salary)
print(income)

def is_rich(income):
    if income > 10000:
        return True
    elif income > 5000:
        return False
    else:
        return False
print(is_rich(income[0]))

def is_rich_match(income):
    match income:
        case True:
            return '是'
        case False:
            return '否'
        case _:
            return '未知'
is_rich_match(income[0])

ls = [1, 2, 3, 4, 5]
for i in ls:
    print(i)
print(len(ls), '长度')

for i in range(len(ls)):
    if i == 3:
        print(ls[i])
