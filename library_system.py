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

    def lend_book(self, book_title: str, student: 'Student') -> bool:
        for book in self.books:
            if book.title == book_title:
                if not book.is_Available:
                    print(f"Error: Book '{book_title}' is not available.")
                    return False
                if book in student.borrowed_books:
                    print(f"Error: Student already borrowed '{book_title}'.")
                    return False
                book.is_Available = False
                student.borrowed_books.append(book)
                return True
        print(f"Error: Book '{book_title}' not found.")
        return False

    def accept_return(self, book_title: str, student: 'Student'):
        for book in student.borrowed_books:
            if book.title == book_title:
                book.is_Available = True
                student.borrowed_books.remove(book)
                return
        print(f"Error: Book '{book_title}' was not borrowed by the student.")

    def search_books(self, query: str) -> list:
        result = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                result.append(book)
        return result

class Student:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book_title: str, library: Library):
        library.lend_book(book_title, self)

    def return_book(self, book_title: str, library: Library):
        library.accept_return(book_title, self)



lib = Library()
lib.add_book("1984", "George Orwell")
lib.add_book("To Kill a Mockingbird", "Harper Lee")
lib.add_book("The Catcher in the Rye", "J.D. Salinger")

student = Student("John Doe")

print("\n--- Before borrow ---")
for book in lib.list_books():
    print(book)
    print("----")

student.borrow_book("1984", lib)
student.borrow_book("1984", lib)  # Tente d'emprunter un livre déjà emprunté

print("\n--- after borrow ---")
for book in lib.list_books():
    print(book)
    print("----")

print("\n--- search of 'George' ---")
for book in lib.search_books("George"):
    print(book)

student.return_book("1984", lib)
student.return_book("1984", lib)  # Tente de retourner un livre déjà retourné

print("\n--- after return ---")
for book in lib.list_books():
    print(book)
    print("----")

