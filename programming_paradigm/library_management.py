# Objective: Solidify understanding of basic OOP concepts in Python by implementing a system 
# that tracks books in a library, focusing on classes, object instantiation, and method invocation.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Sorry, '{title}' is not available or does not exist in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"'{title}' was not checked out or does not exist in the library.")

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")