from injector import Injector
from internal.router import Router
from internal.server.http import Http
# from flask_sqlalchemy import SQLAlchemy
from pkg.sqlalchemy import SQLAlchemy

from config import Config
from module import ExtensionModule

conf = Config()

injector = Injector([ExtensionModule])

app = Http(__name__, conf=conf, db=injector.get(SQLAlchemy), router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)

