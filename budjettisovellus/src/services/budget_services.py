from tkinter import E
from entities.user import User
from repositories.user_repository import UserRepository

class UsernameError(Exception):
    pass

class InvalidUsernameOrPasswordError(Exception):
    pass

class BudgetServices:
    def __init__(self, user_repository):
        self.user_repository = UserRepository

    def login(username, password):
        return False

    def create_user(username, password):
        existing = UserRepository.find_user(username)
        if existing:
            raise UsernameError("Username taken")
        
        user = UserRepository.create_user(User(username, password))
        return user