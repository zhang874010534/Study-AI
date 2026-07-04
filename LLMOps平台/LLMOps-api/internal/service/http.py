import os

from flask import Flask
from pgk.response import json, Response, HttpCode

from internal.exception import CustomException

from internal.router import Router
from config import Config
class Http(Flask):
    def __init__(self, *args, conf: Config, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        router.registerRouter(self)

        # 注册绑定异常错误
        self.register_error_handler(Exception, self._register_error_handler)

        self.config.from_object(conf)

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

