from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

def create_tables(connection):
    cursor = connection.cursor()

def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
