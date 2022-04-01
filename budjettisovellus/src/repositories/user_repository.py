from entities.user import User

class UserRepository:
    def __init__(self):
        self.user_repository = []

    def create(self, username, password):
        self.user_repository.append((username, password))