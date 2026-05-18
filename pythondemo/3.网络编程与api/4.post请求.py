import requests
import json

# headers = {'Content-Type': 'application/json'}
# response = requests.post('https://httpbin.org/post', json={'name': '张三'}, headers=headers)
# json参数无需手动设置请求头设置请求头
response = requests.post('https://httpbin.org/post', json={'name': '张三'})
data = response.json()
print(json.dumps(data, indent=2))
