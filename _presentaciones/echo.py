from cgi import parse_qs
def application(environ, response_callback):
    get = parse_qs(environ['QUERY_STRING'])
    text = get['with'][0] + '\n'
    response_callback(
        "200 OK",
        [('Content-Type', 'text/plain'),
         ('Content-Length', str(len(text)))]
        )
    return [text]
from wsgiref.simple_server import make_server
daemon = make_server('127.0.0.1', 8000, application)
daemon.serve_forever()

