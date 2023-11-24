import Repositories.AuthenticationRepository as AuthenticationRepository
import os
import jwt

from datetime import datetime, timedelta

class AuthenticationHandle:
    def Handle(self, email, password):
        
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