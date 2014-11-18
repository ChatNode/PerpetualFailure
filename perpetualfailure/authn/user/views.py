import logging
log = logging.getLogger(__name__)

from pyramid.httpexceptions import (
    HTTPBadRequest,
    HTTPFound,
    HTTPForbidden,
)
from pyramid.view import view_config

from perpetualfailure.db import session
from perpetualfailure.authn.user import User


@view_config(
    route_name="authentication.login",
    renderer="auth/user.mako")
def authentication_login(request):
    # Ensure that Authenticated users aren't logged in.
    if request.session.user:
        return HTTPFound(location=request.route_path("admin.dashboard"))
    # Pass on login requests.
    if request.POST:
        return do_login(request)
    # sosleepy
    return {}


@view_config(
    route_name="authentication.logout",
)
def autentication_logout(request):
    if not request.session.user:
        return HTTPForbidden()

    headers = request.authn.forget(request)
    return HTTPFound(location=request.route_path("base.home"), headers=headers)


def do_login(request):
    def loginError(message, uid=None):
        logComment = "%s (#%i)" % (message, uid) if uid else message
        log.debug("Failed login attempt from %s: %s.", request.client_addr, logComment)
        return {"error": "Invalid username or password", "debug": message}

    if request.session.user:
        return HTTPFound(location=request.route_path("admin.dashboard"))

    if request.method == "POST":
        if "password" not in request.POST \
                or "username" not in request.POST:
            return HTTPBadRequest()

        # Fetch user from database
        user = session.query(User).filter(User.username == request.POST['username']).first()
        # Verify that the user exists
        if not user: return loginError("No such user")
        # Check if the user actually has a password
        if not user.hash: return loginError("Empty hash field in model", user.id)
        # Verify the user's credentials
        if not request.authn.pass_verify(request.POST['password'], user.hash): return loginError("Hash mismatch", user.id)
        # Authenticate the user
        request.session["auth.uid"] = user.id
        request.authn.remember(request, user.id)
        log.debug("User #%i logged in from %s.", user.id, request.client_addr)
        return HTTPFound(location=request.route_path("admin.dashboard"))

    return {}

