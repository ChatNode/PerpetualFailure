class Navigation(object):
    def __init__(self):
        self.children = []


class Element(object):
    pass


class Link(Element):
    def __init__(self, route, text, **args):
        self.route = route
        self.text = text
        self.args = args


class Menu(Element):
    def __init__(self, text, children, **args):
        self.text = text
        self.args = args
        self.children = children


class Divider(Element):
    pass


# Dictionary to hold navigation instances. Gets added to each request.
navigation = {
    "navbar-left": Navigation(),
}


def configure(config):
    config.add_request_method(lambda x: navigation, "navigation", reify=True)

    def add_link(config, nav="navbar-left", **args):
        if nav not in navigation:
            navigation[nav] = Navigation()
        navigation[nav].children.append(Link(**args))
    config.add_directive("add_navigation_link", add_link, action_wrap=False)

    def add_menu(config, nav="navbar-left", **args):
        if nav not in navigation:
            navigation[nav] = Navigation()
        navigation[nav].children.append(Menu(**args))
    config.add_directive("add_navigation_menu", add_menu, action_wrap=False)