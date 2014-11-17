regex_kb_path = '(/([a-z0-9\-\/]+)?)?'
def configure(config):
    config.add_route('knowledgebase.article.view', "/kb{path:%s}" % regex_kb_path)
    config.add_route('knowledgebase.article.edit', "/admin/kb/edit{path:%s}" % regex_kb_path)
    config.add_route('knowledgebase.article.create', "/admin/kb/create{path:%s}" % regex_kb_path)

