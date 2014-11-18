<%def name="title()">\
%if request.matched_route.name == "news.article.create":
New Article - ChatNode!
%else:
Editing '${article.title}' - ChatNode!\
%endif
</%def>
<%inherit file="/base.mako" />
<form action="${request.route_path(request.matched_route.name, id=article.id)}" method="post">
    <div class="row">
        <div class="col-md-1"></div>
        <div class="col-md-10">
            %if request.matched_route.name == "news.article.create":
            <h1>New news article</h1>
            %else:
            <h1>Editing news article</h1>
            %endif
            <h2><input type="text" name="title" class="col-md-12" value="${article.title}" /></h2>
        </div>
    </div>
    <br />
    <div class="row">
        <div class="col-md-1"></div>
        <div class="col-md-10">
            <textarea class="form-control" rows="20" name="content">${article.content}</textarea><br />
            <input type="submit" class="btn btn-primary" value="Save" />
            <hr />
        </div>
    </div>
</form>
