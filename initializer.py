from users import User
from books import FictionBook, NonFictionBook


class Initializer:
    @staticmethod
    def init_users():
        user1 = User('Kamil')
        user2 = User('Mariusz')
        user3 = User('Dominik')

        users = [user1, user2, user3]

        return users

    @staticmethod
    def init_books():
        book1 = FictionBook('Tytuł', 'Autor', 200,
                            True, 'Horror', 'Wampiry atakują miasto')
        book2 = NonFictionBook('Python', 'Kamil Brzeziński', 300,
                               True, 'Programowanie', 'Początkujący')

        return [book1, book2]
