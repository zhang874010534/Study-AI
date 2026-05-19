import requests
from requests.auth import HTTPBasicAuth
import json

def generate_data():
    for i in range(10):
        yield f'张三{i}'
data = generate_data()
response = requests.post(
    'https://httpbin.org/post',
    data=data,
)
jsonData = response.json()
print(json.dumps(jsonData, indent=2))
print(jsonData['data'])
