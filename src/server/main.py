import vtemplate.controller
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import NotFound
from werkzeug.wrappers import Request, Response


def application(environ, start_response):
    routes = Map([
        Rule('/', endpoint=('Static', 'homepage')),
    ])
    request = Request(environ)
    adapter = routes.bind_to_environ(request.environ)
    try:
        endpoint, values = adapter.match()
        controller = getattr(vtemplate.controller, endpoint[0])()
        getattr(controller, endpoint[1])()
        response = Response(controller.render(), mimetype='text/html')
        return response(environ, start_response)
    except NotFound as e:
        response = Response('404 Page not found', status=404)
        return response(environ, start_response)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(
        '127.0.0.1', 8080, application,
        use_debugger=True, use_reloader=True,
        static_files={'/': '../www/'}
    )
