from aiohttp import web

routes = web.RouteTableDef()

from .handlers import *
# from .views import *
from .server import Server


