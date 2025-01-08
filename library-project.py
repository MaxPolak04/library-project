import sys
from users import UserNotFoundError
from books import BookNotFoundError, BookNotAvailableError
from library import Library
from initializer import Initializer


def display_library_books(library):
    library.display_books()


def display_borrowed_books(user):
    user.display_books()


def borrow_book(user, library):
    title = input("Podaj tytuł książki, którą chcesz wypożyczyć: ")

    try:
        book = library.borrow_book(title)
        user.borrow_book(book)
    except BookNotFoundError:
        print("Książka o takim tytule nie została znaleziona")
    except BookNotAvailableError:
        print("Ta książka została już wypożyczona")


def return_book(user, library):
    title = input("Podaj tytuł książki, którą chcesz zwrócić: ")

    try:
        user.return_book(title)
        library.return_book(title)
    except BookNotFoundError:
        print("Nie posiadasz takiej książki")


def login(users, name):
    for user in users:
        if user.name == name:
            return user

    raise UserNotFoundError


if __name__ == "__main__":
    library = Library()
    users = Initializer.init_users()

    user = None

    while True:
        while user is None:
            try:
                name = input("Podaj imię, żeby się zalogować: ")
                user = login(users, name)
                print("Zalogowałeś się!")
            except UserNotFoundError:
                print("Użytkownik nie został znaleziony")

        print("1. Wyświetl książki w bibliotece")
        print("2. Wyświetl Twoje książki")
        print("3. Wypożycz książkę")
        print("4. Zwróć książkę")
        print("5. Wyloguj się")
        print("6. Zakończ program")

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
            user = None
        elif option == 6:
            sys.exit()
