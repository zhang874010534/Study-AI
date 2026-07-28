# from flask_sqlalchemy import SQLAlchemy
from pkg.sqlalchemy import SQLAlchemy
from injector import Module, Binder

from internal.extension.database_extension import db


class ExtensionModule(Module):
    # 扩展模块依赖注入配置
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        # 未来如果切换测试数据库 直接这样一改就可以了
        # binder.bind(SQLAlchemy, to=test_db)