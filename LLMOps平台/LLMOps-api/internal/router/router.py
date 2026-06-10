from flask import Flask, Blueprint
from internal.handler import AppHandler
class Router:
    def registerRouter(self, app: Flask):
        # 创建蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        app_handler = AppHandler()
        bp.add_url_rule('/ping', view_func=app_handler.ping, methods=['GET'])