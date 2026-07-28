import uuid
from dataclasses import dataclass

from injector import inject
# from flask_sqlalchemy import SQLAlchemy
# 重写SQLAlchemy的auto_commit方法,添加异常处理
from pkg.sqlalchemy import SQLAlchemy

from internal.model import App

@inject
@dataclass
class AppService:
    db: SQLAlchemy
    def create_app(self) -> App:
        with self.db.auto_commit():
            # 创建实体类
            app = App(name='app', account_id=uuid.uuid4(), icon="", description='这是一个简单的聊天机器人')
            # 添加到session会话中
            self.db.session.add(app)
        # 提交session
        # self.db.session.commit()
        return app

    def get_app(self, id: uuid.UUID) -> App:
        app = self.db.session.query(App).get(id)
        return app

    def update_app(self, id: uuid.UUID) -> App:
        with self.db.auto_commit():
            app = self.get_app(id)
            app.name = "gpt聊天机器人"
        # self.db.session.commit()
        return app

    def delete_app(self, id: uuid.UUID) -> App:
        with self.db.auto_commit():
            app = self.get_app(id)
            self.db.session.delete(app)
        return app

