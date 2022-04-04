from entities.user import User

class UserRepository:
    def __init__(self):
        self.users = {}

    def create_user(self, user):
        username = user.username

        if username not in self.users:
            self.users[username] = user
            return "User created"
        else:
            return "User taken"


    def find_user(self, user):
        username = user.username

        if username in self.users:
            return self.users[username]
        else:
            return None


    def find_all_users(self):
        return self.users


    def delete_user(self, user):
        username = user.username
        if username in self.users:
            self.users.pop(username)
            return "User deleted"
        else:
            return None


    def delete_all_users(self):
        self.users = {}


    def __str__(self):
        return f"{self.users}"