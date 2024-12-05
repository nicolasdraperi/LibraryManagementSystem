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

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        with open("library_data.txt", "a") as file:
            file.write(book.title + ',' + book.author + ',' + str(book.is_Available) + '\n')

    def list_books(self):
        return self.books

    def save_books(self, file_path: str):
        with open(file_path, 'w') as file:
            for book in self.books:
                file.write(book.title + ',' + book.author + ',' + str(book.is_Available) + '\n')

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
                    print(f"Error: Book '{book_title}' is not available.")  #texte ecrit par l'autocompleteur
                    return False
                if book in student.borrowed_books:
                    print(f"Error: Student already borrowed '{book_title}'.")  #texte ecrit par l'autocompleteur
                    return False
                book.is_Available = False
                student.borrowed_books.append(book)
                return True
        print(f"Error: Book '{book_title}' not found.")  #texte ecrit par l'autocompleteur
        return False

    def accept_return(self, book_title: str, student: 'Student'):
        for book in student.borrowed_books:
            if book.title == book_title:
                book.is_Available = True
                student.borrowed_books.remove(book)
                return
        print(f"Error: Book '{book_title}' was not borrowed by the student.")  #texte ecrit par l'autocompleteur

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


def run_library_system():
    library = Library()


    try:
        library.load_books("library_data.txt")
        print("Library data loaded successfully from 'library_data.txt'.")
    except FileNotFoundError:
        print("File 'library_data.txt' not found. Starting with an empty library.")

    student = Student("John Doe")

    while True:
        print("\n=== Library Menu ===")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Add a new book")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print("\n--- List of Books ---")
            for book in library.list_books():
                print("Title: " + book.title)
                print("Author: " + book.author)
                print("Available: " + str(book.is_Available))
                print("----")

        elif choice == "2":
            query = input("Enter a title or author to search: ")
            results = library.search_books(query)
            if results:
                print("\n--- Search Results ---")
                for book in results:
                    print("Title: " + book.title)
                    print("Author: " + book.author)
                    print("Available: " + str(book.is_Available))
                    print("----")
            else:
                print("No books found matching the query.")

        elif choice == "3":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            library.add_book(title, author)
            print("Book '" + title + "' by " + author + " has been added and saved.")

        elif choice == "4":
            book_title = input("Enter the title of the book to borrow: ")
            if library.lend_book(book_title, student):
                print("You have successfully borrowed '" + book_title + "'.")
            else:
                print("Unable to borrow '" + book_title + "'. It may be unavailable or not exist.")

        elif choice == "5":
            book_title = input("Enter the title of the book to return: ")
            if book_title in [book.title for book in student.borrowed_books]:
                library.accept_return(book_title, student)
                print("You have successfully returned '" + book_title + "'.")
            else:
                print("You cannot return '" + book_title + "' because you have not borrowed it.")

        elif choice == "6":
            print("Exiting the library system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

run_library_system()