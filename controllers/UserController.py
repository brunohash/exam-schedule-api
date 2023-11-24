class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def get_user(self, user_id):
        return self.user_service.get_user(user_id)

    def get_users(self):
        return self.user_service.get_users()

    def create_user(self, user):
        return self.user_service.create_user(user)

    def update_user(self, user_id, user):
        return self.user_service.update_user(user_id, user)

    def delete_user(self, user_id):
        return self.user_service.delete_user(user_id)