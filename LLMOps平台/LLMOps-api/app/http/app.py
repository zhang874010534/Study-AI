from injector import inject, Injector
from internal.router import Router
from internal.service.http import Http

injector = Injector()

app = Http(__name__, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)

