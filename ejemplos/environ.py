def application(environ, 
        start_response):  
  text = ""
  for k,v in environ.items():
      text += "%s: %s\n"%(k,v)

  start_response(
          "200 OK",
          [('Content-Type', 'text/plain'),
           ('Content-Length', str(len(text)))]
          )
  return [text]

from wsgiref.simple_server import make_server
daemon = make_server('127.0.0.1', 8000, application)
daemon.handle_request()

