from entities.user import User
from entities.purchase import Purchase
from repositories.purchase_repository import PurchaseRepository
from repositories.user_repository import UserRepository

class PurchaseService:
    def __init__(self, purchase_repo= PurchaseRepository, user_repo= UserRepository):
        self.purchase_repo = purchase_repo
        self.user_repo = user_repo

    def create_purchase(self, purchase):
        pass

    def get_purchases(self):
        pass

    def login(self, username, password):
        pass

    def logout(self, username, password):
        pass

    def create_user(self, username, password):
        pass

    def current_user(self):
        pass

    def get_all_users(self):
        pass