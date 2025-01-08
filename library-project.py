import sys
from users import User, UserNotFoundError
from books import FictionBook, NonFictionBook, BookNotFoundError, BookNotAvailableError
from library import Library


def display_library_books(library):
    for book in library.books:
        book.display_book_info()


def display_borrowed_books(user):
    for book in user.books:
        book.display_book_info()


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
    user1 = User('Kamil')
    user2 = User('Mariusz')
    user3 = User('Dominik')

    users = [user1, user2, user3]

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
