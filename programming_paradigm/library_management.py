class Book:
    """
    Represents a single book with a title, author, and checkout status.
    """
    def __init__(self, title, author):
        self.title = title                # public attribute
        self.author = author              # public attribute
        self._is_checked_out = False      # private attribute

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available, otherwise False."""
        return not self._is_checked_out


class Library:
    """
    Represents a library that manages a collection of books.
    """

    def __init__(self):
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        """Adds a Book instance to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book by title.
        Marks the book as unavailable if found.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """
        Returns a book by title.
        Marks the book as available if found.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' was not checked out or not found.")

    def list_available_books(self):
        """
        Prints all available books in the library.
        If none are available, prints a message.
        """
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")
