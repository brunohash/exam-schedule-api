import Controllers.AuthenticationController
import Controllers.ScheduleController
import Middleware.UserMiddleware as UserMiddleware
import json

from dotenv import load_dotenv
load_dotenv()

class Routes:

    

    def request(self, request_handler, path):
        token = request_handler.headers.get('Authorization', '')
        token = token.replace('Bearer ', '')
        middleware = UserMiddleware.UserMiddleware().check_user_token(token)
        type_user = middleware.get('type_id')

        match path:
            case '/users/show':

                content_length = int(request_handler.headers['Content-Length'])
                body = request_handler.rfile.read(content_length).decode('utf-8')
                json_data = json.loads(body)

                email = json_data.get('email', '')
                password = json_data.get('password', '')

                auth =  Controllers.AuthenticationController().login(email, password)
                request_handler.send_response(200)
                request_handler.send_header('Content-Type', 'application/json')
                request_handler.end_headers()
                request_handler.wfile.write(json.dumps(auth).encode('utf-8'))

            case '/login':

                content_length = int(request_handler.headers['Content-Length'])
                body = request_handler.rfile.read(content_length).decode('utf-8')
                json_data = json.loads(body)

                email = json_data.get('email', '')
                password = json_data.get('password', '')

                auth =  Controllers.AuthenticationController.AuthenticationController().login(email, password)
                request_handler.send_response(200)
                request_handler.send_header('Content-Type', 'application/json')
                request_handler.end_headers()
                request_handler.wfile.write(json.dumps(auth).encode('utf-8'))

            case '/register':

                content_length = int(request_handler.headers['Content-Length'])
                body = request_handler.rfile.read(content_length).decode('utf-8')
                json_data = json.loads(body)

                #add type_id in json_data
                json_data['type_user'] = type_user
                json_data['type'] = json_data.get('type', '')

                register = Controllers.AuthenticationController.AuthenticationController().register(json_data)
                
                request_handler.send_response(register.get('code'))
                request_handler.send_header('Content-Type', 'application/json')
                request_handler.end_headers()
                request_handler.wfile.write(json.dumps(register).encode('utf-8'))
            
            case '/schedule':

                if(middleware.get("status") != "success"):

                    request_handler.send_response(400)
                    request_handler.send_header('Content-Type', 'application/json')
                    request_handler.end_headers()
                    request_handler.wfile.write(json.dumps({"status": "error", "message": middleware.get("message")}).encode('utf-8'))
                
                else:

                    content_length = int(request_handler.headers['Content-Length'])
                    body = request_handler.rfile.read(content_length).decode('utf-8')
                    json_data = json.loads(body)
                    schedule = Controllers.ScheduleController.ScheduleController().store(json_data)
                    request_handler.send_response(schedule.get('code'))
                    request_handler.send_header('Content-Type', 'application/json')
                    request_handler.end_headers()
                    request_handler.wfile.write(json.dumps(schedule).encode('utf-8'))
            
            case '/schedule/find':

                if(middleware.get("status") != "success"):

                    request_handler.send_response(400)
                    request_handler.send_header('Content-Type', 'application/json')
                    request_handler.end_headers()
                    request_handler.wfile.write(json.dumps({"status": "error", "message": middleware.get("message")}).encode('utf-8'))
                
                else:

                    content_length = int(request_handler.headers['Content-Length'])
                    body = request_handler.rfile.read(content_length).decode('utf-8')
                    json_data = json.loads(body)
                    schedule = Controllers.ScheduleController.ScheduleController().find(json_data)
                    request_handler.send_response(schedule.get('code'))
                    request_handler.send_header('Content-Type', 'application/json')
                    request_handler.end_headers()
                    request_handler.wfile.write(json.dumps(schedule).encode('utf-8'))
 
            case _:
                request_handler.send_response(404)
                request_handler.send_header('Content-Type', 'application/json')
                request_handler.end_headers()
                request_handler.wfile.write(json.dumps({"status": "error", "message": "Invalid request"}).encode('utf-8'))
