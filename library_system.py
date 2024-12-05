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

    def load_books(self, file_path: str):
        with open(file_path, 'r') as file:
            for line in file:
                # Remove whitespace and split by comma
                line = line.strip()
                if line:  # Ignore empty lines
                    title, author = line.split(',', 1)
                    self.add_book(title.strip(), author.strip())



lib = Library()
lib.load_books("library_data.txt")

books = lib.list_books()
for book in books:
    print(book)
    print("---------")