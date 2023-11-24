# api_controller.py
from http.server import BaseHTTPRequestHandler

import routes


class APIController(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.routes = routes.Routes()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        self.routes.request(self, self.path)
    
if __name__ == '__main__':
    from http.server import HTTPServer

    port = 8000
    server_address = ('', port)

    with HTTPServer(server_address, APIController) as httpd:
        print(f'Serving on port {port}')
        httpd.serve_forever()
