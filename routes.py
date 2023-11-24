from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
import re

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        get_routes = {
            r"/schedule/(\d+)/find": self.handle_schedule_find,
            r"/exams/(\d+)/find": self.handle_exams_find,
            r"/exams/(\d+)/types/find": self.handle_exams_types_find,
            r"/exams/types": self.handle_types_all
        }
        
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        for route, handler in get_routes.items():
            match = re.match(route, path)

            if match:
                if match.group(0) == None:
                    return handler()
                if match.group(1) == None:
                    return handler(match.group(1))
            else:
                return handler()
            
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"Not Found")

    def do_POST(self):
        post_routes = {
            "/login": self.handle_login,
            "/register": self.handle_register,
            "/schedule": self.handle_schedule,
            "/exams": self.handle_exams,
        }

        parsed_url = urlparse(self.path)
        path = parsed_url.path

        if path in post_routes:
            post_routes[path]()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def handle_login(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Handling login..."
        self.wfile.write(message.encode('utf-8'))

    # Implemente outros métodos de manipulação aqui...
    def handle_register(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Handling register..."
        self.wfile.write(message.encode('utf-8'))

    def handle_schedule(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Handling schedule..."
        self.wfile.write(message.encode('utf-8'))

    def handle_schedule_find(self, id):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Handling schedule find..."
        self.wfile.write(message.encode('utf-8'))

    def handle_exams(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Handling exams..."
        self.wfile.write(message.encode('utf-8'))

    def handle_types_all(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Handling exams All..."
        self.wfile.write(message.encode('utf-8'))    

    def handle_exams_types_find(self, id):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Handling exams find..."
        self.wfile.write(message.encode('utf-8'))  
        
    def handle_exams_find(self, id):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Handling exams find..."
        self.wfile.write(message.encode('utf-8'))    

    def handle_exams_types_all(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Handling exams types all..."
        self.wfile.write(message.encode('utf-8'))

    def log_message(self, format, *args):
        # Desativa a saída de logs no console para cada solicitação
        pass
