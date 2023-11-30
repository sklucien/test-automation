from src.services.book_fetcher_service import BookFetcherService
from src.services.book_service import BookService

book_fetcher_service = BookFetcherService()
book_service = BookService(book_fetcher_service=book_fetcher_service)

print('ids : ' +  ', '.join(book_service.list_books_ids()))
print('authors : ' +  ', '.join(book_service.list_books_authors()))
