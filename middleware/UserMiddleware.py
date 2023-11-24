import jwt
import os

class UserMiddleware():
    def check_user_token(self, token):
        try:
            decoded_token = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])

            type_id = decoded_token.get('type')
            print(type_id)

            return {"status": "success", "message": "Token válido", "type_id": int(type_id)}

        except jwt.ExpiredSignatureError:
            return {"status": "error", "message": "Token expirado", "type_id": 3}
        except jwt.InvalidTokenError:
            return {"status": "error", "message": "Token inválido", "type_id": 3}

