import requests
import json

session = requests.Session()
session.headers.update({'User-Agent': '神秘电脑'})
data = {'name': '张三'}
response = requests.post(
    'https://httpbin.org/post',
    data=data,
)
jsonData = response.json()
print(json.dumps(jsonData, indent=2))
print(jsonData['data'])
