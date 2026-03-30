class Book:

    def __init__(self, title, author, num_pages):
        # Initializes a new Book object with title, author, and number of pages.
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        # Returns a string representation of the book, e.g., "'The Hobbit' by J.R.R. Tolkien".
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        # Checks if two books are equal based on title and author.
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        # Checks if one book has fewer pages than another.
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        # Checks if one book has more pages than another.
        return self.num_pages > other.num_pages

    def __add__(self, other):
        # "Adds" two books by summing their page numbers and returning a string.
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        # Checks if a keyword is present in the book's title or author.
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        # Allows accessing book attributes using dictionary-like syntax (e.g., book['title']).
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)  # Calls __str__
print(book1 == book3)  # Calls __eq__
print(book1 < book2)  # Calls ___lt__
print(book2 > book3)  # Calls __gt__
print(book1 + book2)  # Calls __add__
print("Lion" in book3)  # Calls __contains__
print(book3['title'])  # Calls __getitem__