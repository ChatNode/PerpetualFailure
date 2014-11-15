<%inherit file="/base.mako" />
<form action="${action_url}" method="post">
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
