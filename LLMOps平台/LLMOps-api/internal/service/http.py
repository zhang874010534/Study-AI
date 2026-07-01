from flask import Flask
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
        print("异常类型:", type(error))
        print("异常内容 str:", str(error))
        print("异常内容 repr:", repr(error))
        print("异常参数 args:", error.args)
        print("异常属性 dict:", getattr(error, "__dict__", {}))
        return error.message
