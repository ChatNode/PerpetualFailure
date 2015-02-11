from pyramid.authentication import (
    Everyone,
    Authenticated,
)
from pyramid.authorization import (
    Allow,
    Deny,
)


class NewsRoot(object):
    __acl__ = [
        (Allow, Everyone, "view"),
        (Allow, Everyone, "browse"),
        (Allow, Authenticated, "edit"),
        (Allow, Authenticated, "create"),
        (Allow, Authenticated, "list"),
    ]

root = NewsRoot()


def configure(config):
    config.add_root_node("news", root)

    config.add_navigation_link(route="news.article.browse", text="News")

    config.add_route("news.article.view", "/article/{id:[0-9]+}", traverse="/news")
    # Match /article and /article/p{page}
    config.add_route("news.article.browse", "/article", traverse="/news")
    config.add_route("news.article.browse.paged", "/article{page:(/(p[0-9]+)?)?}", traverse="/news")

    config.add_route("news.article.list", "/acp/article", traverse="/news")
    config.add_route("news.article.create", "/acp/article/create", traverse="/news")
    config.add_route("news.article.edit", "/acp/article/edit/{id:[0-9]+}", traverse="/news")
