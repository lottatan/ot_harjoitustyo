import unittest
from entities.user import User
from repositories.user_repository import user_repository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.repo = user_repository
        self.repo.delete_all_users()
        self.user = User("user1", "password123")

    def test_create_user(self):
        new_user = self.repo.create_user(self.user)
        self.assertEqual(new_user, "User created")

    def test_find_user(self):
        self.repo.create_user(self.user)
        user = self.repo.find_user(self.user.username)
        self.assertEqual(user, (self.user.username, self.user.password))

    def test_find_all_users(self):
        self.repo.create_user(self.user)
        users = self.repo.find_all_users()
        amount = len(users)
        self.assertEqual(amount, 1)

    def test_delete_user(self):
        self.repo.create_user(self.user)
        delete = self.repo.delete_user(self.user.username)
        self.assertEqual(delete, "User deleted")

    def test_delete_all_users(self):
        self.repo.create_user(self.user)
        delete = self.repo.delete_all_users()
        self.assertEqual(delete, None)