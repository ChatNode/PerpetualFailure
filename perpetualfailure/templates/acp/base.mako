<%def name="title()">${next.title()} - ${request.registry.settings['perpetualfailure.sitename']} ACP</%def>
<%namespace name="sidebar" file="/sidebar.mako" />
<%inherit file="/base.mako" />
<div class="container-fluid">
    <div class="col-md-2 col-sidebar">
        <ul class="sidebar">
            ${sidebar.render(request, request.navigation['acp'])}\
        </ul>
    </div>
    <div class="col-md-10">
        ${next.body()}
    </div>
