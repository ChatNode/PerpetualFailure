from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    HTTPConflict,
)
from pyramid.view import view_config

from perpetualfailure.db import session
from perpetualfailure.knowledgebase.models import (
    KB_Article,
    KB_ArticleRevision,
)

import copy
import logging
log = logging.getLogger(__name__)


def traverse(path_, page=None, parents=None):
    path = path_
    # We're rolling out blank, let's start from the KB root (index)
    if not page:
        path = copy.copy(path_)
        node = path.pop(0)
        page = session.query(KB_Article).filter(KB_Article.parent == None, KB_Article.name == node).first()
    if not parents:
        parents = []
    # Remove empty elements from the path
    # Lets us do stuff like /kb////channels//// == /kb/channels
    while (path and not path[0]):
        path.pop(0)
    # The path list is empty; we've reache the article we wanted (bottom level)
    if not path:
        return (page, parents)
    # Search for the current path node in the names of this page's children
    node = path.pop(0)
    results = [article for article in page.children if article.name == node]
    if not results:
        # No results found
        return (None, parents)
    # Node found; update page variable and check for more.
    parents.append(page)
    page = results[0]
    return traverse(path, page, parents)


@view_config(
    route_name='knowledgebase.article.view',
    renderer='article/view.mako')
def viewArticle(request):
    path = request.matchdict['path']
    # Check whether we're trying to load the index or not
    if not path or path == "/":
        path = [""]
    else:
        path = path.split("/")

    # The index should always be at the first index in the path
    path[0] = "index"

    # Find the article by traversing the article tree down to the article we
    # want. asdfasdfsa fasdfadsf asdfasdf asdfasfdasd fas sadfasf ghei hei hei
    (article, parents) = traverse(path)
    if not article:
        # Much cri :@(
        return HTTPNotFound()
        # RIP

    revision_count = session.execute("select count(id) from knowledgebase_article_revision where article_id = %i;" % article.id).fetchall()[0][0]

    # Feed the allmighty Mako
    return {"article": article, "parents": parents, "revisions": revision_count}

@view_config(
    route_name='knowledgebase.article.create',
    renderer='article/edit.mako')
def createArticle(request):
    article = KB_Article()
    # Construct a list from the path given in the route URL
    path = request.matchdict['path'].split("/")
    path = [node for node in path if node]
    path.insert(0, "index")
    if len(path) > 1:
        parent = traverse(path[:-1])[0]
        if not parent:
            return HTTPNotFound()
    if traverse(path)[0]:
        return HTTPConflict()

    # Validate data and if appropriate update and redirect.
    r = articleUpdate(request, article, path)
    if isinstance(r, HTTPFound): return r

    url = request.route_path('knowledgebase.article.create', path=request.matchdict['path'])
    return {"article": article, "action_url": url}


@view_config(
    route_name='knowledgebase.article.edit',
    renderer='article/edit.mako')
def editArticle(request):
    # Construct a list from the path given in the route URL
    path = request.matchdict['path'].split("/")
    path = [node for node in path if node]
    path.insert(0, "index")
    article = traverse(path)[0]
    if not article:
        return HTTPNotFound()

    # Validate data and if appropriate update and redirect.
    r = articleUpdate(request, article, path)
    if isinstance(r, HTTPFound): return r

    url = request.route_path('knowledgebase.article.edit', path=request.matchdict['path'])
    return {"article": article, "action_url": url}


def articleUpdate(request, article, path, is_new=False):
    if request.method == 'POST':
        article.title = request.POST['title']
        article.name = path[-1]
        article.content = request.POST['content']
        # Update the parent of this object
        if len(path) > 1:
            article.parent = traverse(path[:-1])[0]
        elif article.parent:
            # This is a root article but it's got a parent, remove the parent
            # from this article object.
            article.parent = None

        curr_rev = KB_ArticleRevision(article)
        prev_rev = article.revision
        if prev_rev:
            prev_rev.children.append(curr_rev)
            session.add(prev_rev)
        session.add(curr_rev)
        article.revision = curr_rev

        session.add(article)
        return HTTPFound(location=request.route_path('knowledgebase.article.view', path=request.matchdict['path']))

