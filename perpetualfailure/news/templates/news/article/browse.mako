<%def name="title()">News - ChatNode!</%def>
<%inherit file="/base.mako" />
<div class="row">
    <div class="col-md-1"></div>
    <div class="col-md-8">
        %for article in news:
        <div class="article">
            <h1><a href="${request.route_path("news.article.view", id=article.id)}">${article.title}</a> <small>\
%if request.permits("edit", context=article):
<a href="${request.route_path("news.article.edit", id=article.id)}"><span class="glyphicon glyphicon-small glyphicon-pencil"></span></a>\
%endif
</small></h1>
            <small><em>Posted ${article.date}</em></small>
            <div class="alert alert-cancer">${article.content|request.md}</div>
        </div>
        <hr />
        %endfor
        <nav>
            <ul class="pager">\
%if has_older_page:
                <li class="previous"><a href="${request.route_path("news.article.browse.paged", page=int(request.matchdict['page']) + 1)}"><span aria-hidden="true">&larr;</span> Older</a></li>
%endif
%if request.matchdict['page'] != '0':
                <li class="next"><a href="${request.route_path("news.article.browse.paged", page=int(request.matchdict['page']) - 1)}">Newer <span aria-hidden="true">&rarr;</span></a></li>
%endif
            </ul>
        </nav>
    </div>
</div>
