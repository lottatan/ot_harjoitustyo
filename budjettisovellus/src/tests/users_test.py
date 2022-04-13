import unittest
from entities.user import User
from entities.purchase import Purchase
from repositories.user_repository import user_repository
from repositories.purchase_repository import purchase_repository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repository = user_repository
        self.user_repository.delete_all_users()

        self.purchase_repository = purchase_repository
        self.purchase_repository.delete_all_purchases_from_all_users()

        self.user = User("user1", "password123")
        self.purchase = Purchase("milk", "2.0", "groceries", self.user.username)

    def test_create_user(self):
        new_user = self.user_repository.create_user(self.user)
        self.assertEqual(new_user, "User created")

    def test_find_user(self):
        self.user_repository.create_user(self.user)
        user = self.user_repository.find_user(self.user.username)
        self.assertEqual((user.username, user.password),
                         (self.user.username, self.user.password))

    def test_find_all_users(self):
        self.user_repository.create_user(self.user)
        users = self.user_repository.find_all_users()
        amount = len(users)
        self.assertEqual(amount, 1)

    def test_delete_user(self):
        self.user_repository.create_user(self.user)
        delete = self.user_repository.delete_user(self.user.username)
        self.assertEqual(delete, "User deleted")

    def test_delete_all_users(self):
        self.user_repository.create_user(self.user)
        delete = self.user_repository.delete_all_users()
        self.assertEqual(delete, None)

    def test_add_purchase(self):
        self.user_repository.create_user(self.user)
        add = self.purchase_repository.add_purchase(self.purchase)
        self.assertEqual(add, "Purchase added")

    def test_show_all_purchases(self):
        self.user_repository.create_user(self.user)
        self.purchase_repository.add_purchase(self.purchase)
        show_all = self.purchase_repository.show_all_purchases(self.purchase.username)
        amount = len(show_all)
        self.assertEqual(amount, 1)

    def test_delete_all_purchases(self):
        self.user_repository.create_user(self.user)
        self.purchase_repository.add_purchase(self.purchase)
        delete = self.purchase_repository.delete_all_purchases(self.purchase.username)
        self.assertEqual(delete, "All purchases deleted")