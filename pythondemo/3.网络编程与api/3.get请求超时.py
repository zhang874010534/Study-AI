import requests
import json
try:
    response = requests.get('https://httpbin.org/delay/2', timeout=1)
except requests.exceptions.Timeout:
    print('请求超时')
except requests.exceptions.RequestException as e:
    print(e)
print(requests.exceptions.Timeout)
