from services.string_service import to_lowercase
from services.user_fetcher_service import UserFetcherService


class UserService:
    user_fetcher_service: UserFetcherService

    def __init__(self, user_fetcher_service: UserFetcherService):
        self.user_fetcher_service = user_fetcher_service

    def list_users(self):
        users = self.user_fetcher_service.get_users()
        return list(map(lambda user: { 'id': user['id'], 'email': to_lowercase(user['email'])}, users))