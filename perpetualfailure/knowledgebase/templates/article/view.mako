<%def name="title()">${article.title} - ChatNode!</%def>
<%inherit file="/base.mako" />
<%!
%>
<div class="row">
    <div class="col-md-1"></div>
    <div class="col-md-8">
        <h1>${article.title} <small><a href="${request.route_path("knowledgebase.article.edit", path=article.path())}"><span class="glyphicon glyphicon-small glyphicon-pencil"></span></a></small></h1>
    </div>
</div>
<div class="row">
    <div class="col-md-1"></div>
    <div class="col-md-8">
        <ol class="breadcrumb">
            %for article_ in sorted(parents, key=lambda x: x.title.lower()):
            <li><a href="${request.route_path("knowledgebase.article.view", path=article_.path())}">${article_.title}</a></li>
            %endfor
            <li class="active">${article.title}</li>
        </ol>
        <div class="article-content">
            ${article.content|request.md}
        </div>
        <hr />
        <small class="glyphicon-small">Last updated ${article.revision.time}</small>
    </div>
    <div class="col-md-2">
        %if article.children:
        <div class="panel panel-default">
            <div class="panel-heading">
                <h2 class="panel-title">Further reading</h2>
            </div>
            <div class="panel-body panel-table">
                <ul>
                    %for article_ in article.children:
                    <li><a href="${request.route_path("knowledgebase.article.view", path=article_.path())}">${article_.title}</a></li>
                    %endfor
                </ul>
            </div>
        </div>
        %endif
        <div class="panel panel-default">
            <div class="panel-heading">
                <h2 class="panel-title">${revisions} revisions</h2>
            </div>
            <div class="panel-body">
                This revision is ${request.relative_date(article.revision.time)} old.
            </div>
        </div>
    </div>
</div>
