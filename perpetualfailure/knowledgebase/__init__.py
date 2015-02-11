regex_kb_path = '(/([a-z0-9\-\/]+)?)?'
def configure(config):
    config.add_navigation_link(route="knowledgebase.article.view", text="Knowledge base", path="")

    config.add_route('knowledgebase.article.view', "/kb{path:%s}" % regex_kb_path)
    # TODO: Create a root factory and allow "create" and "edit" for
    # pyramid.authentication.Authenticated
    config.add_route('knowledgebase.article.edit', "/acp/kb/edit{path:%s}" % regex_kb_path)
    config.add_route('knowledgebase.article.create', "/acp/kb/create{path:%s}" % regex_kb_path)

