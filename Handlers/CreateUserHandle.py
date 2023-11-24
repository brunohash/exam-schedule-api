import Repositories.AuthenticationRepository as AuthenticationRepository

class CreateUserHandle:
    def Handle(self, data):
        
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