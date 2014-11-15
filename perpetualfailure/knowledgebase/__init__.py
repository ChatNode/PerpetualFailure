def configure(config):
    config.add_route('knowledgebase.article.view', "/kb{path:(/([a-z0-9\/]+)?)?}")
    config.add_route('knowledgebase.article.edit', "/admin/kb/edit{path:(/([a-z0-9\/]+)?)?}")
    config.add_route('knowledgebase.article.create', "/admin/kb/create{path:(/([a-z0-9\/]+)?)?}")

