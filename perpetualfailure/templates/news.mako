<%inherit file="/base.mako" />
<div class="row">
    <div class="col-md-1"></div>
    <div class="col-md-8">
        %for article in news:
        <div class="article">
            <h1>${article.title}</h1>
            <em>Posted ${article.date}</em>
            <div class="alert alert-cancer">${article.content|request.md}</div>
        </div>
        <hr />
        %endfor
    </div>
    %if False:
    <div class="col-md-2">
        <div class="panel panel-default">
            <div class="panel-heading">
                <h3 class="panel-title">Submit new article</h3>
            </div>
            <div class="panel-body">
                <form method="post">
                    <div class="form-group">
                        <label for="title">Tittel</label>
                        <input id="title" class="form-control" name="title" />
                    </div>
                    <div class="form-group">
                        <label for="content">Innhold</label>
                        <textarea id="content" class="form-control" name="content" style="height: 200px;"></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary" >Post</button>
                </form>
            </div>
        </div>
        %endif
    </div>
</div>
