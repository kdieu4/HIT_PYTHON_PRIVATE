from model.book import Book


class Library:
    def __init__(self):
        self.books = [Book]

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book.get_id() == book_id:
                self.books.remove(book)
        return None

    def find_book(self, title_or_author):
        for book in self.books:
            if book.get_title() == title_or_author or book.get_author() == title_or_author:
                return book
        return None

    def borrow_book(self, book_id):
        for book in self.books:
            if book.get_id() == book_id:
                if book.get_status() == "Borrowed":
                    book.set_status("Borrowed")
                else:
                    print("This book is already borrowed!")

    def return_book(self, book_id):
        for book in self.books:
            if book.get_id() == book_id:
                if book.get_status() == "Borrowed":
                    book.set_status("Returned")
