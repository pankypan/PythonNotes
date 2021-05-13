from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello Web!</h1>']


if __name__ == '__main__':
    httpd = make_server('', 8080, application)
    print("Serving HTTP on port 8080...")
    httpd.serve_forever()
