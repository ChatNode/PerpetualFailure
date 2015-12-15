from pyramid.response import Response
from pyramid.security import Authenticated
from pyramid.view import view_config
from datetime import datetime


def configure(config):
    config.add_route('base.home', "/")
    config.add_route('admin.dashboard', "/acp")


@view_config(
    route_name='base.home',
    renderer='home.mako',
)
def base_home(request):
    return {}

@view_config(
    route_name='admin.dashboard',
    renderer='acp/dashboard.mako',
    permission=Authenticated,
)
def admin_dashboard(request):
    return {}

