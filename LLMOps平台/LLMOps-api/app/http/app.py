from injector import inject, Injector, Module, Binder
from internal.router import Router
from internal.service.http import Http
from internal.extension.database_extension import db
from flask_sqlalchemy import SQLAlchemy

from config import Config
from module import ExtensionModule

conf = Config()


injector = Injector([ExtensionModule])

app = Http(__name__, conf=conf, db=injector.get(SQLAlchemy), router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)

