<%def name="title()">Login</%def>
<%inherit file="/base.mako" />
<form action="${request.route_path("authentication.login")}" method="post">
<input name="username" type="text" class="form-control" placeholder="Username" /><br />
<input name="password" type="password" class="form-control" placeholder="Password" /><br />
<input type="submit" class="btn btn-primary" value="Log in" />
</form>
