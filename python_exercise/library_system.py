#task1
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True  

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Available: {self.is_available}"
#task2
class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, title: str, author: str):
        new_book = Book(title, author)  
        self.books.append(new_book)  

    def list_books(self):
        return [str(book) for book in self.books]  
    
    #task3
    def load_books(self, file_path: str):
        with open(file_path, 'r') as file:
            for line in file:
                 title, author = line.strip().split(',')  
                 self.add_book(title, author)  



    #task4
    class Student:
        def __init__(self, name: str):
            self.name = name
            self.borrowed_books = []  

        def borrow_book(self, book_title: str, library: Library):
            book = next((b for b in library.books if b.title == book_title and b.is_available), None)
            if book:
                library.lend_book(book_title, self)  
                self.borrowed_books.append(book)  
            else:
                print(f"The book '{book_title}' is not available.")


    #task5
    def lend_book(self, book_title: str, student: Student) -> bool:
        book = next((b for b in self.books if b.title == book_title and b.is_available), None)
        if book:
            book.is_available = False  
            return True
        return False

    def accept_return(self, book_title: str, student: Student):
        book = next((b for b in student.borrowed_books if b.title == book_title), None)
        if book:
            book.is_available = True  
            student.borrowed_books.remove(book)  


    #task6
    def borrow_book(self, book_title: str, library: Library):
        if len(self.borrowed_books) >= 3:  
            print(f"{self.name} cannot borrow more than 3 books.")
            return
        if book_title in [book.title for book in self.borrowed_books]:
            print(f"{self.name} already borrowed '{book_title}'.")
            return
        super().borrow_book(book_title, library)  


    #task7

    def search_books(self, query: str):
        return [str(book) for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]

    #task8
    def save_books(self, file_path: str):
        with open(file_path, 'w') as file:
            for book in self.books:
                file.write(f"{book.title},{book.author}\n")

    def load_books(self, file_path: str):
        with open(file_path, 'r') as file:
            for line in file:
                title, author = line.strip().split(',')
                self.add_book(title, author)
    #task9
    def run_library_system():
        library = Library()
        library.load_books("library_data.txt")  # Load initial books.

        while True:
            print("Library Menu:")
            print("1. View all books")
            print("2. Search for a book")
            print("3. Add a new book")
            print("4. Borrow a book")
            print("5. Return a book")
            print("6. Exit")
        
            choice = input("Enter your choice: ")
        
            if choice == "1":
                for book in library.list_books():
                    print(book)
            elif choice == "2":
                query = input("Enter book title or author to search: ")
                results = library.search_books(query)
                for result in results:
                    print(result)
            elif choice == "3":
                title = input("Enter book title: ")
                author = input("Enter author: ")
                library.add_book(title, author)
            elif choice == "4":
                student_name = input("Enter student name: ")
                book_title = input("Enter book title: ")
                student = Student(student_name)
                student.borrow_book(book_title, library)
            elif choice == "5":
                student_name = input("Enter student name: ")
                book_title = input("Enter book title: ")
                student = Student(student_name)
                student.return_book(book_title, library)
            elif choice == "6":
                print("Exiting program.")
                break



    #task10
    def borrow_book(self, book_title: str, library: Library):
        if len(self.borrowed_books) >= 3:
            print(f"Cannot borrow more than 3 books.")
            return
        if book_title in [book.title for book in self.borrowed_books]:
            print(f"{book_title} is already borrowed.")
            return
        book = next((b for b in library.books if b))
        
