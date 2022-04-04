from entities.user import User
from repositories.user_repository import UserRepository

def main():
    repo = UserRepository()
    user = User("user1", "password123")

    repo.create_user(user)

    print(repo)

if __name__ == "__main__":
    main()