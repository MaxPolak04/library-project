from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, author, pages, available):
        self.title = title
        self.author = author
        self.pages = pages
        self.available = available

    @abstractmethod
    def display_concrete_book_info(self):
        pass

    def display_book_info(self):
        print(f'Tytuł: {self.title}')
        print(f'Autor: {self.author}')
        print(f'Liczba stron: {self.pages}')
        self.display_concrete_book_info()
        print(f"Dostępna? {'tak' if self.available else 'Nie'}")


class NonFictionBook(Book):
    def __init__(self, title, author, pages, available, subject, level):
        super().__init__(title, author, pages, available)
        self.subject = subject
        self.level = level

    def display_concrete_book_info(self):
        print(f'Temat: {self.subject}')
        print(f'Poziom: {self.level}')


class FictionBook(Book):
    def __init__(self, title, author, pages, available, genre, synopsis):
        super().__init__(title, author, pages, available)
        self.genre = genre
        self.synopsis = synopsis

    def display_concrete_book_info(self):
        print(f'Gatunek: {self.genre}')
        print(f'Streszczenie: {self.synopsis}')


class BookNotFoundError(Exception):
    pass


class BookNotAvailableError(Exception):
    pass
