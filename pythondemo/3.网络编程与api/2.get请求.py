import requests
import json
response = requests.get('https://httpbin.org/get', params={'name': '张三'})
if response.status_code == 200:
    data = response.json()
    print(data)
    print(json.dumps(data,indent=2))