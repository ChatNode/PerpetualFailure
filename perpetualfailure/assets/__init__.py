def configure(config):
    config.add_static_view('js', 'assets/js', cache_max_age=3600)
    config.add_static_view('fonts', 'assets/fonts', cache_max_age=3600)

    config.add_route('css', '/css/{css_path:[^_][^/]*}.css')
    config.add_view(route_name='css', view='pyramid_scss.controller.get_scss', renderer='scss', request_method='GET')
