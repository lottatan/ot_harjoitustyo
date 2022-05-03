from entities.user import User
from entities.purchase import Purchase
from database_connection import get_database_connection


def purchase_by_row(row):
    return Purchase(
        row["purchase"], row["price"], row["category"], row["username"]
    ) if row else None


class PurchaseRepository:
    """Luokka, joka vastaa ostosten tietokannasta
    """

    def __init__(self, connection):
        """Konstruktori, joka antaa polun tietokantaan

        Args:
            connection: polku tietokantaan
        """
        self._connection = connection

    def show_all_purchases(self, username):
        """Näyttää kaikki käyttäjän ostokset.

        Args:
            username (str): sisäänkirjautuneen käyttäjän käyttäjänimi

        Returns:
            purchases: palauttaa listan sisäänkirjautuneen käyttäjän ostoksista
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT purchase, price, category, username FROM Purchases WHERE username= ?",
            [username])
        rows = cursor.fetchall()

        purchases = []
        for row in rows:
            purchases.append((row["purchase"], row["price"], row["category"]))

        return purchases

    def add_purchase(self, purchase):
        """Lisää ostoksen tietokantaan

        Args:
            purchase (Purchase): Purchase-olion tyyppinen ostos

        Returns:
            "Purchase added" : viesti siitä, että ostos on lisätty
        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Purchases (purchase, price, category, username) VALUES (?, ?, ?, ?)", [
                       purchase.purchase,
                       purchase.price,
                       purchase.category,
                       purchase.username])
        self._connection.commit()

        return "Purchase added"

    def show_sum(self, username):
        """Näyttää ostosten yhteenlasketun summan

        Args:
            username (str): _sisäänkirjautuneen käyttäjän käyttäjänimi

        Returns:
            sum: ostosten yhteenlaskettu summa
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT SUM(price) as sum FROM Purchases WHERE username= ?", [username])
        sum = cursor.fetchone()

        return sum["sum"]

    def delete_all_purchases(self, username):
        """Poistaa käyttäjän kaikki ostokset tietokannasta

        Args:
            username (str): sisäänkirjautuneen käyttäjän käyttäjänimi

        Returns:
            "All purchases deleted": viesti, että kaikki ostokset on poistettu
        """
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Purchases WHERE username= ?", [username])
        self._connection.commit()

        return "All purchases deleted"

    def delete_all_purchases_from_all_users(self):
        """Poistaa tietokannasta kaikkien käyttäjien ostokset
        """
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Purchases")
        self._connection.commit()


purchase_repository = PurchaseRepository(get_database_connection())
