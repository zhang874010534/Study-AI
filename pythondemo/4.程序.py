name = '张三'
age = 18
per_salary = 200

def get_income(name, day, per_salary):
    return day * per_salary
income = get_income(name, 20, per_salary)
print(income)