import os
from asyncio import log

from flask import request
from openai import OpenAI
from internal.schema.app_schema import CompletionReq
from pkg.response import Response, HttpCode, success_json, validation_json
from flask import jsonify
from internal.exception import FailException

api_key = os.getenv("ARK_API_KEY")
client = OpenAI(base_url="https://ark.cn-beijing.volces.com/api/v3", api_key=api_key)
class AppHandler:

    def completion(self):
        query = request.json.get("query")
        req = CompletionReq(query=query)
        if not req.validate():
            return validation_json(req.errors)

        response = client.responses.create(
            model="ep-20260707230632-rnsh2",
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

        content = response.output[1].content[0].text
        print(response)
        resp = Response(
            code=HttpCode.SUCCESS,
            message="success",
            data={
                "content": content,
            }
        )
        return success_json({
            "content": content,
        }), 200
    def ping(self):
        raise FailException("ping failed")
        return {
            "ping": "pong"
        }