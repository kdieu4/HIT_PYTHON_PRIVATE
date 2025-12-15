from model.book import Book
from service.library import Library

lib = Library()


def run():
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        handle_add_book()

    elif choice == "2":
        handle_remove_book()


def show_menu():
    print("---BOOK MANAGER---")
    print("1. Add book")
    print("2. Remove book by id")
    print("3. Search book by title or author")
    print("4. Borrow book")
    print("5. Return book")
    print("6. Exit")


def handle_add_book():
    book_id = input("Enter book id: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter book year: ")
    status = input("Enter book status: ")
    book = lib.add_book(Book(id, title, author, year, status))


def handle_remove_book():
    book_id = input("Enter book id: ")
    lib.remove_book(book_id)

def handle_search_book():
    book_id = input("Enter book id: ")
    lib.ser_book(book_id)
run()
