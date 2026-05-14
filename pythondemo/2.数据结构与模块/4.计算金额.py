from decimal import Decimal, getcontext
# getcontext().prec = 2
employee = [
    {
        'name': '张三',
        'base': 1000,
        'bonus': 100
    },
    {
        'name': '李四',
        'base': 1000,
        'bonus': 50
    },
    {
        'name': '王五',
        'base': 1000,
        'bonus': 60
    }
]
total = 0
for item in employee:
    total += item['base'] + item['bonus']
print(total)
print(f"平均金额为：{total/len(employee)}")
print(0.1 + 0.2)

result = Decimal(16.12) + Decimal(14.27)
print(result)

decimalResult = Decimal("0.1") + Decimal("0.2")
print(decimalResult)
print(decimalResult == Decimal("0.3"))

