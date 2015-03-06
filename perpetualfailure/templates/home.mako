<%def name="title()">${request.registry.settings['perpetualfailure.sitename']}</%def>
<%inherit file="/base.mako" />
<div class="row">
    <div class="col-md-1"></div>
    <div class="col-md-10">
        <h1>This is the default frontpage</h1>
        This means that you either haven't made your own <code>home.mako</code>
        template, or that the <code>perpetualfailure.views.base</code> module
        is shadows your own view or is being used instead of a customized
        <code>base.home</code> view callable.
    </div>
</div>
