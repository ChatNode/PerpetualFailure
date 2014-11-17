from datetime import datetime

from pyramid.config import Configurator
from pyramid.decorator import reify
from pyramid.request import Request
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


def main(global_config, **settings):
    ## Prepare database
    engine = engine_from_config(settings, 'sqlalchemy.')
    db.session.configure(bind=engine)
    db.Base.metadata.bind = engine
    #

    config = Configurator(settings=settings, request_factory=RequestFactory)
    ## Load and configure all views
    for path in settings['chatnode.modules'].split("\n"):
        module = __import__(path, fromlist=[path])
        module.configure(config)
        config.scan(module)
    #
    return config.make_wsgi_app()
