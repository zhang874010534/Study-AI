import re

people_data = [
    {
        "name": "张三",
        "phone": "13812345678",          # 正确
        "email": "zhangsan@example.com", # 正确
        "id_card": "110105199001011234", # 正确格式
    },
    {
        "name": "李四",
        "phone": "15898765432",          # 正确
        "email": "lisi@qq.com",          # 正确
        "id_card": "32031119880520321X", # 正确格式
    },
    {
        "name": "王五",
        "phone": "18866668888",          # 正确
        "email": "wangwu@163.com",       # 正确
        "id_card": "440106200012123456", # 正确格式
    },

    {
        "name": "赵六",
        "phone": "23812345678",          # 错误：不是1开头
        "email": "zhaoliu@example.com",  # 正确
        "id_card": "110105199001011234", # 正确格式
    },
    {
        "name": "孙七",
        "phone": "1381234567",           # 错误：只有10位
        "email": "sunqi@qq.com",         # 正确
        "id_card": "32031119880520321X", # 正确格式
    },
    {
        "name": "周八",
        "phone": "138123456789",         # 错误：12位
        "email": "zhouba@163.com",       # 正确
        "id_card": "440106200012123456", # 正确格式
    },

    {
        "name": "吴九",
        "phone": "13911112222",          # 正确
        "email": "wujiuexample.com",     # 错误：缺少@
        "id_card": "110105199001011234", # 正确格式
    },
    {
        "name": "郑十",
        "phone": "13622223333",          # 正确
        "email": "zhengshi@",            # 错误：@后面为空
        "id_card": "32031119880520321X", # 正确格式
    },
    {
        "name": "钱一",
        "phone": "13733334444",          # 正确
        "email": "@example.com",         # 错误：@前面为空
        "id_card": "440106200012123456", # 正确格式
    },

    {
        "name": "冯二",
        "phone": "13544445555",          # 正确
        "email": "fenger@example.com",   # 正确
        "id_card": "110105199913011234", # 错误：月份13
    },
    {
        "name": "陈三",
        "phone": "13455556666",          # 正确
        "email": "chensan@qq.com",       # 正确
        "id_card": "110105199901001234", # 错误：日期00
    },
    {
        "name": "褚四",
        "phone": "13366667777",          # 正确
        "email": "chusi@163.com",        # 正确
        "id_card": "110105199901321234", # 错误：日期32
    },

    {
        "name": "蒋五",
        "phone": "138-1234-5678",        # 错误：含横线
        "email": "jiangwu example@qq.com", # 错误：含空格
        "id_card": "11010519900101123A", # 错误：最后一位不是数字或X
    },
    {
        "name": "沈六",
        "phone": "+8613812345678",       # 错误：带国家码
        "email": "shenliu@qq",           # 错误：没有顶级域名
        "id_card": "1101051990010112X4", # 错误：X不在最后一位
    },
    {
        "name": "韩七",
        "phone": "13812345abc",          # 错误：含字母
        "email": "hanqi@@example.com",   # 错误：两个@
        "id_card": "11010519900101 234", # 错误：含空格
    },
]
# 手机号：1开头，第二位3-9，总共11位
phone_pattern = re.compile(r'^1[3-9]\d{9}$')

# 邮箱：简单校验，要求 xxx@xxx.xxx
email_pattern = re.compile(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$')

# 身份证：18位，前17位数字，最后一位可以是数字或X/x
# 同时简单校验年月日格式
id_card_pattern = re.compile(
    r'^[1-9]\d{5}'
    r'(18|19|20)\d{2}'
    r'(0[1-9]|1[0-2])'
    r'(0[1-9]|[12]\d|3[01])'
    r'\d{3}[\dXx]$'
)

for person in people_data:
    name = person["name"]

    phone = person["phone"]
    email = person["email"]
    id_card = person["id_card"]

    if not phone_pattern.match(phone):
        print(f"{name} 手机号不合规：{phone}")

    if not email_pattern.match(email):
        print(f"{name} 邮箱不合规：{email}")

    if not id_card_pattern.match(id_card):
        print(f"{name} 身份证不合规：{id_card}")