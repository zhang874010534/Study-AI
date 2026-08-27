import os
from asyncio import log

from flask import request, Flask
from injector import inject
from openai import OpenAI
from internal.schema.app_schema import CompletionReq
from pkg.response import Response, HttpCode, success_json, validation_json, success_message
from flask import jsonify
from internal.exception import FailException
from internal.service import AppService
from dataclasses import dataclass
import uuid

api_key = os.getenv("ARK_API_KEY")
client = OpenAI(base_url="https://ark.cn-beijing.volces.com/api/v3", api_key=api_key)
@inject
@dataclass
class AppHandler:

    app_service: AppService
    def create_app(self):
        app = self.app_service.create_app()
        return success_message(f"应用已经成功创建,应用ID为{app.id}")
    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f'应用{app.name}已经成功获取')
    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f'应用{app.name}已经成功更新')
    def completion(self):
        query = request.json.get("query")
        req = CompletionReq(query=query)
        if not req.validate():
            return validation_json(req.errors)

        response = client.responses.create(
            model="ep-20260827220313-29tvz",
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