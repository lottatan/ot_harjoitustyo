from entities.user import User
from entities.purchase import Purchase
from repositories.user_repository import UserRepository
from database_connection import get_database_connection

def purchase_by_row(row):
    return Purchase(row["purchase"], row["price"], row["category"], row["username"]) if row else None

class PurchaseRepository:
    def __init__(self, connection):
        self._connection = connection

    def show_all_purchases(self, username):
        cursor = self._connection.cursor()

        cursor.execute("SELECT purchase, price, category, username FROM Purchases WHERE username= ?", [username])
        rows = cursor.fetchall()

        purchases = []
        for row in rows:
            purchases.append((row["purchase"], row["price"], row["category"]))

        return purchases

    def add_purchase(self, purchase):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Purchases (purchase, price, category, username) VALUES (?, ?, ?, ?)", [
                       purchase.purchase, purchase.price, purchase.category, purchase.username])
        self._connection.commit()

        return "Purchase added"


    def delete_all_purchases(self, username):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Purchases WHERE username= ?", [username])
        self._connection.commit()

        return "All purchases deleted"

    def delete_all_purchases_from_all_users(self):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Purchases")
        self._connection.commit()


purchase_repository = PurchaseRepository(get_database_connection())