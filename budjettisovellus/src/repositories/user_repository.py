from entities.user import User
from database_connection import get_database_connection


def user_by_row(row):
    return User(row["username"], row["password"], row["budget"]) if row else None


class UserRepository:
    """Tietokanta, jossa on kaikki käyttäjätiedot
    """

    def __init__(self, connection):
        """Konstruktori, joka antaa polun tietokantaan

        Args:
            connection: polku tietokantaan
        """        
        self._connection = connection

    def create_user(self, user):
        """luo uuden käyttäjän

        Args:
            user (User): User-olion tyyppinen käyttäjä

        Returns:
            "User created": viesti, että käyttäjä on luotu
        """        
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Users (username, password, budget) VALUES (?, ?, ?)", [
                       user.username, user.password, user.budget])
        self._connection.commit()

        return "User created"

    def find_user(self, username):
        """Etsii käyttäjänimen perusteella, että onko käyttäjää olemassa

        Args:
            username (str): käyttäjänimi

        Returns:
            User: palauttaa käyttäjän, jos sellainen on olemassa ja None jos ei ole
        """        
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Users WHERE username= ?", [username])
        row = cursor.fetchone()

        if row:
            return user_by_row(row)
        return None

    def find_all_users(self):
        """Etsii kaikki käyttäjät

        Returns:
            list: lista kaikista tietokannassa olemassa olevista käyttäjistä
        """        
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()

        return list(map(user_by_row, rows))

    def set_new_budget(self, budget, username):
        """Asettaa uuden budjetin käyttäjälle

        Args:
            budget (int): uuden budjetin koko
            username (str): sisäänkirjautuneen käyttäjän käyttäjänimi

        Returns:
            text: viesti, että budjetti on päivitetty
        """        
        cursor = self._connection.cursor()

        cursor.execute("UPDATE Users SET budget= ? WHERE username= ?", [
                       budget, username])
        self._connection.commit()

        return "Budget updated"

    def delete_user(self, username):
        """Poistaa käyttäjän

        Args:
            username (str): sisäänkirjautuneen käyttäjän käyttäjänimi

        Returns:
            text: viesti, että käyttäjä on poistettu
        """        
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Users WHERE username= ?", [username])
        cursor.execute("DELETE FROM Purchases WHERE username= ?", [username])

        return "User deleted"

    def delete_all_users(self):
        """Poistaa kaikki tietokannassa olemassa olevat käyttäjät
        """        
        cursor = self._connection

        cursor.execute("DELETE FROM Users")
        cursor.execute("DELETE FROM Purchases")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
users = user_repository.find_all_users()
