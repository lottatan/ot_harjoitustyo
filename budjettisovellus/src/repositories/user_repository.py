from entities.user import User
from database_connection import get_database_connection


def user_by_row(row):
    return User(row["username"], row["password"]) if row else None

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", [user.username, user.password])
        self._connection.commit()

        return "User created"

    def find_user(self, username):
        cursor = self._connection.cursor()
        
        cursor.execute("SELECT * FROM Users WHERE username= ?", [username])
        row = cursor.fetchone()

        return user_by_row(row)

    def find_all_users(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT * FROM Users")
        rows = cursor.fetchall()

        return list(map(user_by_row, rows))

    def delete_user(self, user):
        cursor = self._connection.cursor()

        cursor.execute("DELETE * FROM Users WHERE username= ?", [user.username])
        self._connection.fetchall()

        return "User deleted"

    def delete_all_users(self):
        cursor = self._connection

        cursor.execute("DELETE * FROM Users")
        self._connection.commit()

user_repository = UserRepository(get_database_connection())
users = user_repository.find_all_users()