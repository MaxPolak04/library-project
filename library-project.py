import sys
from users import User
from books import FictionBook, NonFictionBook
from library import Library


def display_library_books(library):
    for book in library.books:
        book.display_book_info()


def display_borrowed_books(user):
    for book in user.books:
        book.display_book_info()


def borrow_book(user, library):
    title = input("Podaj tytuł książki, którą chcesz wypożyczyć: ")

    book = library.borrow_book(title)
    user.borrow_book(book)


def return_book(user, library):
    title = input("Podaj tytuł książki, którą chcesz zwrócić: ")

    user.return_book(title)
    library.return_book(title)


if __name__ == "__main__":
    library = Library()
    user = User('Maks')

    while True:
        print("1. Wyświetl książki w bibliotece")
        print("2. Wyświetl Twoje książki")
        print("3. Wypożycz książkę")
        print("4. Zwróć książkę")
        print("5. Zakończ program")

        option = int(input("Wybierz opcję: "))

        if option == 1:
            display_library_books(library)
        elif option == 2:
            display_borrowed_books(user)
        elif option == 3:
            borrow_book(user, library)
        elif option == 4:
            return_book(user, library)
        elif option == 5:
            sys.exit()
