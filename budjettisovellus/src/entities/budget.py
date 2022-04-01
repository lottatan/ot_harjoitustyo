from repositories.purchase_repository import PurchaseRepository

class Budget:
    def __init__(self):
        self.budget = 0
        self.used = PurchaseRepository.used()

    def edit_budget(self, budget):
        self.budget = budget

    def remaining_budget(self):
        self.remaining = self.budget - self.used
