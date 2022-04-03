import unittest
from entities.user import User
from repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user = User("user1", "password123")

    def test_create_user(self):
        UserRepository.create_user(self.user)

        self.assertEqual(UserRepository.findall()[-1].username, self.user)

    

    