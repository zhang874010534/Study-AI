from injector import inject, Injector
from internal.router import Router
from internal.service.http import Http

from config import Config
conf = Config()
injector = Injector()

app = Http(__name__, conf=conf, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)

