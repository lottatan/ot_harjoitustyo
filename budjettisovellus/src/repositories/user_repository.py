from entities.user import User
from database_connection import get_database_connection


def user_by_row(row):
    return User(row["username"], row["password"], row["budget"]) if row else None


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Users (username, password, budget) VALUES (?, ?, ?)", [
                       user.username, user.password, user.budget])
        self._connection.commit()

        return "User created"

    def find_user(self, username):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Users WHERE username= ?", [username])
        row = cursor.fetchone()

        if row:
            return user_by_row(row)
        else:
            return None

    def find_all_users(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()

        return list(map(user_by_row, rows))

    def set_new_budget(self, budget, username):
        cursor = self._connection.cursor()

        cursor.execute("UPDATE Users SET budget= ? WHERE username= ?", [budget, username])
        self._connection.commit()

    def delete_user(self, username):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Users WHERE username= ?", [username])
        cursor.execute("DELETE FROM Purchases WHERE username= ?", [username])

        return "User deleted"

    def delete_all_users(self):
        cursor = self._connection

        cursor.execute("DELETE FROM Users")
        cursor.execute("DELETE FROM Purchases")
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
users = user_repository.find_all_users()
