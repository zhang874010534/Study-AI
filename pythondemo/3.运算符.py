# Python 运算符学习

# 1. 算术运算符
print("=== 算术运算符 ===")
a = 10
b = 3
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")  # 加法
print(f"a - b = {a - b}")  # 减法
print(f"a * b = {a * b}")  # 乘法
print(f"a / b = {a / b}")  # 除法（浮点数）
print(f"a // b = {a // b}")  # 整除
print(f"a % b = {a % b}")  # 取模
print(f"a ** b = {a ** b}")  # 幂运算

# 2. 比较运算符
print("\n=== 比较运算符 ===")
print(f"a == b: {a == b}")  # 等于
print(f"a != b: {a != b}")  # 不等于
print(f"a > b: {a > b}")  # 大于
print(f"a < b: {a < b}")  # 小于
print(f"a >= b: {a >= b}")  # 大于等于
print(f"a <= b: {a <= b}")  # 小于等于

# 3. 逻辑运算符
print("\n=== 逻辑运算符 ===")
x = True
y = False
print(f"x = {x}, y = {y}")
print(f"x and y: {x and y}")  # 与
print(f"x or y: {x or y}")  # 或
print(f"not x: {not x}")  # 非

# 4. 赋值运算符
print("\n=== 赋值运算符 ===")
c = 5
print(f"初始 c = {c}")
c += 3  # 等价于 c = c + 3
print(f"c += 3 后: {c}")
c -= 2  # 等价于 c = c - 2
print(f"c -= 2 后: {c}")
c *= 4  # 等价于 c = c * 4
print(f"c *= 4 后: {c}")
c /= 2  # 等价于 c = c / 2
print(f"c /= 2 后: {c}")

# 5. 成员运算符
print("\n=== 成员运算符 ===")
list1 = [1, 2, 3, 4, 5]
print(f"列表: {list1}")
print(f"3 in list1: {3 in list1}")  # 检查元素是否在列表中
print(f"6 not in list1: {6 not in list1}")  # 检查元素是否不在列表中

# 6. 身份运算符
print("\n=== 身份运算符 ===")
d = [1, 2, 3]
e = d  # 引用同一个对象
f = [1, 2, 3]  # 创建新对象
print(f"d = {d}, e = {e}, f = {f}")
print(f"d is e: {d is e}")  # 检查是否是同一个对象
print(f"d is f: {d is f}")  # 检查是否是同一个对象
print(f"d == f: {d == f}")  # 检查值是否相等

# 7. 位运算符（二进制操作）
print("\n=== 位运算符 ===")
g = 60  # 二进制: 00111100
h = 13  # 二进制: 00001101
print(f"g = {g}, h = {h}")
print(f"g & h = {g & h}")  # 按位与
print(f"g | h = {g | h}")  # 按位或
print(f"g ^ h = {g ^ h}")  # 按位异或
print(f"~g = {~g}")  # 按位取反
print(f"g << 2 = {g << 2}")  # 左移
print(f"g >> 2 = {g >> 2}")  # 右移


if a > b and a < 10:
    print("a 大于 b 且小于 10")
else:
    print("a 不大于 b 或大于等于 10")
