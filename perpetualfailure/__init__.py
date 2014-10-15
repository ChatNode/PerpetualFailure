from pyramid.config import Configurator
from pyramid.decorator import reify
from pyramid.request import Request
from sqlalchemy import engine_from_config

import bleach
import markdown

import perpetualfailure.db as db


class RequestFactory(Request):
    def md(self, text):
        return bleach.clean(markdown.markdown(text, output_format="html5"), tags=['p', 'hr', 'a', 'code', 'img', 'pre', 'blockquote', 'li', 'lo', 'strong', 'em'])


def main(global_config, **settings):
    ## Prepare database
    engine = engine_from_config(settings, 'sqlalchemy.')
    db.session.configure(bind=engine)
    db.Base.metadata.bind = engine
    #

    config = Configurator(settings=settings, request_factory=RequestFactory)
    ## Load and configure all views
    for path in settings['chatnode.modules'].split("\n"):
        view = __import__(path, fromlist=[path])
        view.configure(config)
        config.scan(view)
    #
    return config.make_wsgi_app()
