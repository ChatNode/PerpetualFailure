<%def name="title()">Login</%def>
<%inherit file="/base.mako" />
<%namespace name="t_auth" file="/auth/widgets.mako" />
<div class="row">
    <div class="col-md-3"></div>
    <div class="col-md-6">
        <div class="login-padding">
            %if error:
            <div class="alert alert-danger" role="alert"><strong>Couldn't log you in:</strong> ${error}</div>
            %endif
        </div>
        <div class="panel panel-info">
            <div class="panel-heading">
                <h3 class="panel-title">Login</h3>
            </div>
            <div class="panel-default">
                <div class="panel-heading">
                    Please provide your account credentials
                </div>
            </div>
            <div class="panel-body">
                ${t_auth.login_form()}
            </div>
        </div>
    </div>
</div>
