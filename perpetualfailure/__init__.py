from datetime import datetime

from pyramid.config import Configurator
from pyramid.decorator import reify
from pyramid.request import Request
from pyramid.security import (
    Allow,
    Authenticated,
)
from pyramid.authorization import ACLAuthorizationPolicy
from sqlalchemy import engine_from_config

import bleach
import markdown

import perpetualfailure.db as db


class RequestFactory(Request):
    def md(self, text):
        return bleach.clean(markdown.markdown(text, output_format="html5"), tags=['p', 'hr', 'a', 'code', 'img', 'pre', 'blockquote', 'li', 'lo', 'strong', 'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'], attributes={"a":["href"],"img":['src','alt']})

    def relative_date(self, time):
        # TODO: Move this to somewhere else.
        date = []
        delta = datetime.utcnow() - time
        if delta.days > 0:
            if delta.days != 1:
                suffix = "s"
            else:
                suffix = ""
            date.append("%s day%s" % (delta.days, suffix))

        hours = (delta.seconds//3600) % 24
        if hours > 0:
            if hours != 1:
                suffix = "s"
            else:
                suffix = ""
            date.append("%s hour%s" % (hours, suffix))

        minutes = (delta.seconds//60) % 60
        if minutes != 1:
            suffix = "s"
        else:
            suffix = ""
        date.append("%s minute%s" % (minutes, suffix))

        return ", ".join(date)


class Root(object):
    __acl__ = [
        (Allow, Authenticated, Authenticated),
    ]
    nodes = {}

    def __init__(self, request):
        self.request = request

    @classmethod
    def add_node(cls, name, obj):
        cls.nodes[name] = obj

    def __getitem__(self, key):
        node = self.nodes[key]
        node.__parent__ = self
        node.__name__ = key
        return node


def request_test_permission(request, permission, context=None):
    """Short-hand method for testing permissions against the current user.
    By default this uses the context given by the request but this can be
    overridden through the context argument."""
    if not context:
        context = request.context
    return request.authz.permits(context, request.authn.effective_principals(request), permission)


def main(global_config, **settings):
    ## Prepare database
    engine = engine_from_config(settings, 'sqlalchemy.')
    db.session.configure(bind=engine)
    db.Base.metadata.bind = engine
    #

    # FIXME: Pyramid whines about no configured authorization policy, probably
    # because we didn't set authn policy using the Configurator initializer.
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(
        settings=settings,
        root_factory=Root,
        request_factory=RequestFactory,
        authorization_policy=authz_policy,
    )
    # Expose the authorization policy through requests.
    config.add_request_method(lambda x: authz_policy, "authz", reify=True)
    # Add a configurator method to add new nodes to the root factory
    config.add_directive("add_root_node", Root.add_node, action_wrap=False)
    # Provide a short-hand method for testing permissions.
    config.add_request_method(request_test_permission, "permits")
    ## Load and configure all views
    for path in settings['chatnode.modules'].split("\n"):
        module = __import__(path, fromlist=[path])
        module.configure(config)
        config.scan(module)
    #
    return config.make_wsgi_app()
