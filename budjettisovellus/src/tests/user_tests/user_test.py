import unittest 
from entities.user import User
from entities.purchase import Purchase
from entities.budget import Budget

class TestUser(unittest.TestCase):
    def setup(self):
        self.user = User()

    def test_user_is_real(self):
        self.assertNotEqual(self.user, None)

    def test_username_is_correct(self, username):
        self.assertEqual(self.user.username, username)

    def test_password_is_correct(self, password):
        self.assertEqual(self.user.password, password)


class TestBudget(unittest.Testcase):
    def setup(self):
        self.budget = Budget()

    def test_budget_is_correct(self, budget):
        self.assertEqual(self.budget.budget, budget)