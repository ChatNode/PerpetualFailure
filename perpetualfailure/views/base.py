from pyramid.response import Response
from pyramid.view import view_config
from datetime import datetime


def configure(config):
    config.add_route('base.home', "/")


@view_config(
    route_name='base.home',
    renderer='home.mako',
)
def base_home(request):
    return {}

