from datetime import datetime

from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPException,
    HTTPBadRequest,
    HTTPFound,
    HTTPNotFound,
)

from perpetualfailure.db import session
from perpetualfailure.news.models import News_Article


@view_config(
    route_name='news.article.browse',
    renderer='news/article/browse.mako',
    permission='browse',
)
@view_config(
    route_name='news.article.browse.paged',
    renderer='news/article/browse.mako',
    permission='browse',
)
def article_browse(request):
    news = session.query(News_Article).order_by(News_Article.date.desc()).all()
    return {"news": news}


@view_config(
    route_name='news.article.view',
    renderer='news/article/view.mako',
    permission='view',
)
def article_view(request):
    article = session.query(News_Article).filter(News_Article.id == request.matchdict['id']).first()
    if not article:
        return HTTPNotFound()
    return {"article": article}


@view_config(
    route_name='news.article.edit',
    renderer='news/article/edit.mako',
    permission='edit',
)
def article_edit(request):
    article = session.query(News_Article).filter(News_Article.id == request.matchdict['id']).first()

    r = articleUpdate(request, article)
    if isinstance(r, HTTPException):
        return r

    return {"article": article}


@view_config(
    route_name='news.article.create',
    renderer='news/article/edit.mako',
    permission='create',
)
def article_create(request):
    article = News_Article()

    r = articleUpdate(request, article)
    if isinstance(r, HTTPException):
        return r

    return {"article": article}


def articleUpdate(request, article):
    if request.method != "POST":
        return None

    for key in ['title', 'content']:
        if key not in request.POST:
            return HTTPBadRequest()

    article.title = request.params['title']
    article.content = request.params['content']
    article.date = datetime.utcnow()
    session.add(article)
    session.flush()
    return HTTPFound(location=request.route_path('news.article.view', id=article.id))
