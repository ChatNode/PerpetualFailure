from pyramid.response import Response
from pyramid.view import view_config
from datetime import datetime

from perpetualfailure.db import Article, session


def configure(config):
    config.add_route('base.home', "/")
    config.add_route('base.news', "/news")


@view_config(route_name='base.home', renderer='home.mako')
def base_home(request):
    return {}

@view_config(route_name='base.news', renderer='news.mako')
def my_view(request):
    if False and "title" in request.params and "content" in request.params:
        article = Article()
        article.title = request.params['title']
        article.content = request.params['content']
        article.date = datetime.utcnow()
        session.add(article)
    news = session.query(Article).order_by(Article.date.desc()).all()
    return {"news": news}
