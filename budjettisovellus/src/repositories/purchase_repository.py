#Tänne tallennetaan kaikki tehdyt ostokset

class PurchaseRepository:
    def __init__(self):
        self.purchases = []
        self.used = 0

    def show_all_by_username(self):
        pass

#lisätään ostos muodossa (tyyppi, hinta)
    def add_purchase(self, purchase):
        self.purchases.append(purchase)
        self.used += purchase[1]

    def delete_purchase(self, purchase):
        self.purchases.remove(purchase)
        self.used -= purchase[1]

    def delete_all_purchases(self):
        self.purchases = []
        self.used = 0