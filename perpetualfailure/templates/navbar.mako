<%!
# Includes used for instance matching
from perpetualfailure.navigation import Link
%>


<!-- The request variable becomes available for all subsequently called functions -->
<%def name="render(request, nav)">\
%for child in nav.children:
${render_el(child)}
%endfor
</%def>


<%def name="render_el(el)">\
%if isinstance(el, Link):
${render_link(el)}\
%endif
</%def>


<%def name="render_link(el)"><li><a href="${request.route_path(el.route, **el.args)}">${el.text}</a></li></%def>
