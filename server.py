# api_controller.py
from http.server import BaseHTTPRequestHandler
from Routes import Handler

if __name__ == '__main__':
    from http.server import HTTPServer

    port = 8000
    server_address = ('', port)

    with HTTPServer(server_address, Handler) as httpd:
        print(f'Serving on port {port}')
        httpd.serve_forever()
