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

    def lend_book(self, book_title: str, student: "Student") -> bool:
        for book in self.books:
            if book.title == book_title and book.is_Available:
                book.is_Available = False
                student.borrowed_books.append(book)
                return True
        return False

    def accept_return(self, book_title: str, student: "Student"):
        for book in student.borrowed_books:
            if book.title == book_title:
                book.is_Available = True
                student.borrowed_books.remove(book)
                return

class Student:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book_title: str, library: Library):
        for book in library.books:
            if book.title == book_title and book.is_Available:
                book.is_Available = False
                self.borrowed_books.append(book)
                break

    def return_book(self, book_title: str, library: Library):
        for book in library.books:
            if book.title == book_title:
                book.is_Available = True
                self.borrowed_books.remove(book)
                break



lib = Library()
lib.add_book("1984", "George Orwell")
lib.add_book("To Kill a Mockingbird", "Harper Lee")

student = Student("John Doe")

print("\n--- Before borrow ---")
for book in lib.list_books():
    print(book)
    print("----")

lib.lend_book("1984", student)

print("\n--- After borrow ---")
for book in lib.list_books():
    print(book)
    print("----")

print("\n--- books borowed by jhon ---")
for book in student.borrowed_books:
    print(book)

lib.accept_return("1984", student)

print("\n--- after borrow ---")
for book in lib.list_books():
    print(book)
    print("----")

