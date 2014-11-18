from pyramid.authentication import (
    Authenticated,
    Everyone,
    SessionAuthenticationPolicy,
)
from pyramid.authorization import Allow
from pyramid.events import (
    NewRequest,
    subscriber,
)
from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from perpetualfailure.db import session, Base


policy = None


def configure(config):
    policy = UserAuthenticationPolicy()
    # Set the authentication policy
    config.set_authentication_policy(policy)
    # Add property request.authn
    def get_policy(request):
        return policy
    config.add_request_method(get_policy, "authn", reify=True)

    config.add_route('authentication.login', "/acp/login")
    config.add_route('authentication.logout', "/acp/logout")


@subscriber(NewRequest)
def request_session_inject_user(event):
    request = event.request
    request.session.user = None

    uid = request.authn.authenticated_userid(request)
    if uid:
        request.session.user = session.query(User) \
            .filter(User.id == uid).first()


class User(Base):
    __tablename__ = "authn_user"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(Text, nullable=False)
    hash = Column(Text)

    @property
    def __acl__(self):
        return [
            (Allow, "u:%i" % self.id, "edit"),
            (Allow, "g:admin", "edit"),
        ]



class UserAuthenticationPolicy(SessionAuthenticationPolicy):
    from passlib.hash import bcrypt_sha256 as passlib

    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)

    def authenticated_userid(self, request):
        uid = self.unauthenticated_userid(request)
        user = session.query(User).filter(User.id == uid).first()
        if user:
            return user.id
        return None

    def effective_principals(self, request):
        """ Sequence of current user id, user groups, and system groups
            (Everyone, Authenticated)
        """
        user = None
        if request.session.user:
            user = request.session.user
        principals = set([Everyone])

        if not user:
            return principals

        principals.add(Authenticated)
        return principals

    def pass_verify(self, password, hash):
        return self.passlib.verify(password, hash)

    def pass_generate(self, password):
        return self.passlib.encrypt(password)
