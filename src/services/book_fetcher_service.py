import requests


class BookFetcherService:
    def get_books(self):
        r = requests.get('http://localhost:1080/books')
        return r.json()