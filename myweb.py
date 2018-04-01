#!/usr/bin/env python
from wsgiref.simple_server import make_server  
def application(environ, start_response):  
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Welcome to  IT training course @SiChuan Tianfu IDC 2018.03.38 !</h1>']
httpd = make_server('', 80, application) 
print('Serving HTTP on port 80...')

httpd.serve_forever() 