class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Check out this book."""
        self._is_checked_out = True

    def return_book(self):
        """Return this book."""
        self._is_checked_out = False

    def is_available(self):
        """Check if book is available."""
        return not self._is_checked_out

    def __str__(self):
        status = "Checked out" if self._is_checked_out else "Available"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        book = self.find_book(title)
        if book and book.is_available():
            book.check_out()
            print(f"Checked out: {title}")
        elif book:
            print(f"Book '{title}' is already checked out.")
        else:
            print(f"Book '{title}' not found.")

    def return_book(self, title):
        """Return a book by title."""
        book = self.find_book(title)
        if book and not book.is_available():
            book.return_book()
            print(f"Returned: {title}")
        elif book:
            print(f"Book '{title}' was not checked out.")
        else:
            print(f"Book '{title}' not found.")

    def find_book(self, title):
        """Find a book by title."""
        for book in self._books:
            if book.title == title:
                return book
        return None

    def list_available_books(self):
        """List all available books."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")