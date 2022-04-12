from entities.user import User
from repositories.user_repository import user_repository as default_user_repository


class UsernameError(Exception):
    pass


class InvalidUsernameOrPasswordError(Exception):
    pass


class BudgetServices:
    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

    def login(self, username, password):
        user = self._user_repository.find_user(username)
        if not user or user.password != password:
            raise InvalidUsernameOrPasswordError(
                "Incorrect username or password")

        self._user = user

        return user

    def create_user(self, username, password):
        existing = self._user_repository.find_user(username)
        if existing:
            raise UsernameError("Username taken")

        user = self._user_repository.create_user(User(username, password))
        return user

    def get_current_user(self):
        return self._user

    def delete_user(self, username):
        self._user_repository.delete_user(username)


budget_services = BudgetServices()
