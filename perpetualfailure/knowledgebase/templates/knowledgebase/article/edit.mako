<%def name="title()">\
%if request.matched_route.name == "knowledgebase.article.create":
Creating '/kb${request.matchdict['path']}' - ChatNode!\
%else:
Editing '${article.title}' - ChatNode!\
%endif
</%def>
<%inherit file="/base.mako" />
<form action="${request.route_path(request.matched_route.name, path=request.matchdict['path'])}" method="post">
    <div class="row">
        <div class="col-md-1"></div>
        <div class="col-md-8">
            <h1><input type="text" name="title" class="col-md-12" value="${article.title}" /></h1>
        </div>
    </div>
    <br />
    <div class="row">
        <div class="col-md-1"></div>
        <div class="col-md-8">
            <textarea class="form-control" rows="20" name="content">${article.content}</textarea><br />
            <input type="submit" class="btn btn-primary" value="Save" />
            <hr />
        </div>
    </div>
</form>
