from initialize_database_connection import initialize_database


def pytest_configure():
    initialize_database()
