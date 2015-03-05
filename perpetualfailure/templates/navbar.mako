<%!
# Includes used for instance matching
from perpetualfailure.navigation import (
    Divider,
    Link,
    Menu,
)
%>


<!-- The request variable becomes available for all subsequently called functions -->
<%def name="render(request, nav)">\
%for child in nav.children:
${render_el(child)}
%endfor
</%def>


<%def name="render_el(el, do_menu=True)">\
%if isinstance(el, Link):
${render_link(el)}\
%elif isinstance(el, Menu) and do_menu:
${render_menu(el)}
%elif isinstance(el, Divider):
<li class="divider"></li>
%endif
</%def>


<%def name="render_link(el)"><li><a href="${request.route_path(el.route, **el.args)}">${el.text}</a></li></%def>

<%def name="render_menu(el)"><li><a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false">${el.text} <span class="caret"></span></a>
<ul class="dropdown-menu">
%for child in el.children:
${render_el(child, do_menu=False)}\
%endfor
</ul>
</li></%def>
