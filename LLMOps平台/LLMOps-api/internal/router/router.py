from flask import Flask, Blueprint
from internal.handler import AppHandler
from injector import inject
from dataclasses import dataclass

@inject
@dataclass
class Router:
    app_handler: AppHandler

    # def __init__(self, app_handler: AppHandler):
    #     self.app_handler = app_handler

    def registerRouter(self, app: Flask):
        # 创建蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        # app_handler = AppHandler()
        bp.add_url_rule('/ping', view_func=self.app_handler.ping, methods=['GET'])
        bp.add_url_rule('/app/completion', view_func=self.app_handler.completion, methods=['POST'])

        # 注册蓝图
        app.register_blueprint(bp)
