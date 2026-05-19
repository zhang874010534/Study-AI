import requests
from requests.auth import HTTPBasicAuth
import json

login_data = {'username': '张三', 'password': '123456'}
response = requests.post(
    'https://httpbin.org/post',
    data=login_data,
    auth= ('username', 'password')
)
data = response.json()
print(json.dumps(data, indent=2))
