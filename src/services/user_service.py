from entities.user import User
from repositories.user_repository import user_repository as default_user_repository

class UserService:

    def __init__(self):
        self._user_repository = default_user_repository
        self._user = None

    def login(self, username, password):
        user = self._user_repository.check_user_credentials(username, password)
        if not user:
            return False
            print("login - false")

        self._user = user
        return True


    def logout(self):
        self._user = None

    def register(self, username, password, password_again):
        if self._user_repository.check_existing_user(username):
            return False

        self._user_repository.new_user(username, password)
        return True

    def get_id(self):
        return self._user.get_id()

user_service = UserService()