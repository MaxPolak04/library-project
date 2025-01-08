from books import FictionBook, NonFictionBook, BookNotFoundError, BookNotAvailableError


class Library:
    def __init__(self):
        self.books = []

        book1 = FictionBook('Tytuł', 'Autor', 200,
                            True, 'Horror', 'Wampiry atakują miasto')
        book2 = NonFictionBook('Python', 'Kamil Brzeziński', 300,
                               True, 'Programowanie', 'Początkujący')

        self.books.append(book1)
        self.books.append(book2)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                return book
            elif book.title == title and not book.available:
                raise BookNotAvailableError

        raise BookNotFoundError

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                return

