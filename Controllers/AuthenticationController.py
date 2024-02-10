from Handlers.CreateUserHandle import CreateUserHandle
from Handlers.AuthenticationHandle import AuthenticationHandle

class AuthenticationController:
    def __init__(self):
        pass

    def login(self, email, password):
        return AuthenticationHandle().Handle(email, password);
    
    def register(self, data):
        return CreateUserHandle().Handle(data);