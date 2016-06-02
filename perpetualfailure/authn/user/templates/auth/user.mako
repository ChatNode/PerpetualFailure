<%def name="title()">Login</%def>
<%inherit file="/base.mako" />
<%namespace name="t_auth" file="/auth/widgets.mako" />
%if error:
<div class="alert alert-danger" role="alert"><strong>Couldn't log you in:</strong> ${error}</div>
%endif
${t_auth.login_form()}
