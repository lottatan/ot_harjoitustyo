from pathlib import Path
import os

from entities.purchase import Purchase
from repositories.user_repository import UserRepository


class PurchaseRepository:
    def __init__(self):
        pass

    def show_all(self, username):
        pass

# lisätään ostos muodossa (id, tyyppi, hinta)
    def add_purchase(self, purchase, username):
        pass

    def delete_purchase(self, purchase_id, username):
        pass

    def delete_all_purchases(self, username):
        pass
