from repositories.purchase_repository import PurchaseRepository

class Budget:
    def __init__(self):
        self.budget = 0
        self.used = PurchaseRepository.used()

    def edit_budget(self, budget):
        self.budget = budget

    def remaining_budget(self):
        if self.budget - self.used >= 0:
            self.remaining = self.budget - self.used
        else:
            self.remaining = 0
