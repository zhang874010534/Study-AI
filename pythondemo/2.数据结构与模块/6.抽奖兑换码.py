import random
# 12位兑换码 生成兑换码
code = "".join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=12))
print(code)
