from aiohttp import web
# routes = web.RouteTableDef()
from . import routes
# from .views import *
from sqlalchemy import engine

class Server:

    def __init__(self):
        self.app = web.Application()
        self.app.add_routes(routes)


    def run(self):
        web.run_app(self.app)