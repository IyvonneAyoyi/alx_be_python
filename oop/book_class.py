class Book:
    """A class to represent a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Constructor: Initializes a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """String representation for readable output."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation for recreating the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor: Called when the object is deleted."""
        print(f"Deleting {self.title}")
