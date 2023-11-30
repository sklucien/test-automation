import requests


class UserFetcherService:
    def get_users(self):
        r = requests.get('http://localhost:1080/users')
        return r.json()