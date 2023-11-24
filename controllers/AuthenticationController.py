from Handlers.CreateUserHandle import CreateUserHandle
from Handlers.LoginHandle import LoginHandle

class AuthenticationController:
    def __init__(self):
        pass

    def login(self, email, password):
        return LoginHandle().Handle(email, password);
        
    
    def register(self, data):
        return CreateUserHandle().Handle(data);