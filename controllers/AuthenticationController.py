import Repositories.AuthenticationRepository as AuthenticationRepository
import jwt
import os

from datetime import datetime, timedelta

class AuthenticationController:
    def __init__(self):
        pass

    def login(self, email, password):

        auth = AuthenticationRepository.AuthenticationRepository().auth(email, password)

        if auth:
            token_payload = {
                "user_id": auth.get('id'),
                "name": auth.get('name'),
                "email": auth.get('email'),
                "type": auth.get('type_id'),
                "exp": datetime.utcnow() + timedelta(days=1) 
            }
            
            jwt_secret = os.getenv("JWT_SECRET")
            token = jwt.encode(token_payload, jwt_secret, algorithm="HS256")

            return {"status": "success", "code": 201, "message": "Login successful", "token": token}
        
        else:
            return {"status": "error", "code": 401, "message": "Invalid credentials"}
    
    def register(self, data):
        required_fields = ['name', 'email', 'age', 'phoneNumber', 'address', 'password']

        if any(data.get(field) == '' for field in required_fields):
            response = {"status": "error", "code": 400, "message": "All fields are required"}
        else:
            insert = AuthenticationRepository.AuthenticationRepository().store(data)

            if insert.get('status') == 'success':
                response = {"status": "success", "code": 201, "message": "Register successful"}
            else:
                response = {"status": "error", "code": 400, "message": insert.get('message')}

        return response