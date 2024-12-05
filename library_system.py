class Book:
    def __init__(self, title, author, is_Available=True):
        self.title = title
        self.author = author
        self.is_Available = is_Available

    def __str__(self):
        return "title: " + self.title + "\nauthor: " + self.author + "\nis available: " + str(self.is_Available)

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, title: str, author: str):
        self.books.append(Book(title, author))

    def list_books(self):
        return self.books



lib = Library()
lib.add_book("JJBA", "Araki")
lib.add_book("JJBA", "Araki")
lib.add_book("JJBA", "Araki")
lib.add_book("JJBA", "Araki")

books = lib.list_books()
for book in books:
    print(book)