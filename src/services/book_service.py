class BookService:
    def __init__(self, book_fetcher_service):
        self.book_fetcher_service = book_fetcher_service

    def list_books_ids(self):
        books = self.book_fetcher_service.get_books()
        return list(map(lambda book: book['id'], books))

    def list_books_authors(self):
        books = self.book_fetcher_service.get_books()

        return list(set(map(lambda book: book['author']['lastname'] + ' ' + book['author']['firstname'], books)))