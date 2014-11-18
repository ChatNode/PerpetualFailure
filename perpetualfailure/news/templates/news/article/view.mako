<%def name="title()">${article.title} - ChatNode!</%def>
<%inherit file="/base.mako" />
<div class="row">
    <div class="col-md-1"></div>
    <div class="col-md-10">
        <h1>${article.title} <small>\
%if request.permits("edit", context=article):
<a href="${request.route_path("news.article.edit", id=article.id)}"><span class="glyphicon glyphicon-small glyphicon-pencil"></span></a>\
%endif
</small></h1>
    </div>
</div>
<div class="row">
    <div class="col-md-1"></div>
    <div class="col-md-10">
        <small><em>Posted ${article.date}</em></small>
        <div class="alert">${article.content|request.md}</div>
        <hr />
    </div>
</div>
