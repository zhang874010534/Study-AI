import os

from flask import Flask
from pkg.response import json, Response, HttpCode

from internal.exception import CustomException

from internal.router import Router
from config import Config
# from flask_sqlalchemy import SQLAlchemy
from pkg.sqlalchemy import SQLAlchemy

from internal.model import App

class Http(Flask):
    def __init__(self, *args, conf: Config, db: SQLAlchemy, router: Router, **kwargs):
        super().__init__(*args, **kwargs)

        self.config.from_object(conf)

        # 注册绑定异常错误
        self.register_error_handler(Exception, self._register_error_handler)

        # 初始化数据库
        db.init_app(self)
        with self.app_context():
            # 创建数据库表
            # _ = App()
            db.create_all()

        router.registerRouter(self)

    def _register_error_handler(self, error: Exception):
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data else {}
            ))
        print(self.debug, '----------')
        print(os.getenv("FLASK_ENV"), '----')
        if self.debug or os.getenv("FLASK_ENV") == "development":
            raise error
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data={}
            ))

