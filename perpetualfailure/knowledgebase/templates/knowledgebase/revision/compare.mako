<%def name="compare_text()">Comparing \
%if base.article.id == head.article.id:
{${base.id}} and {${head.id}} of article "${head.article.title}"\
%else:
"${base.article.title}"{${base.id}} and "${head.article.title}"{${head.id}}\
%endif
</%def>
<%def name="title()">${compare_text()} - ChatNode!</%def>
<%inherit file="/base.mako" />
<div class="row">
    <div class="col-md-1"></div>
    <div class="col-md-10">
        <h1>${compare_text()}</h1>
    </div>
</div>
<div class="row">
    <div class="col-md-1"></div>
    <div class="col-md-10">
        <div class="article-content">
            <pre>${raw_diff}</pre>
        </div>
        <hr />
    </div>
</div>
