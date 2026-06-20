import os

from flask import request
from openai import OpenAI

api_key = os.getenv("ARK_API_KEY")
client = OpenAI(base_url="https://ark.cn-beijing.volces.com/api/v3", api_key=api_key)
class AppHandler:
    def completion(self):
        query = request.json.get("query")
        response = client.responses.create(
            model="doubao-seed-1-8-251228",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": query,
                        },
                    ],
                }
            ]
        )
        print(response)
        return response.output[1].content[0].text
    def ping(self):
        return {
            "ping": "pong"
        }