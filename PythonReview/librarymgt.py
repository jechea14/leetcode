class Book:
    def __init__(self, title, author, isbn, copies) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    # getters and setters
    def get_title(self) -> str:
        return self.title

    def set_title(self, title) -> None:
        self.title = title

    def get_copies(self):
        return self.copies

    def set_copies(self, amount) -> None:
        self.copies = amount

    def take_book(self) -> bool:
        if self.copies == 0:
            print("no copies available")
            return False
        else:
            self.set_copies(self.get_copies() - 1)
            return True

    def return_book(self) -> None:
        self.set_copies(self.get_copies() + 1)


class Member:
    def __init__(self, name, member_id) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    # getters and setters
    def get_name(self) -> str:
        return self.name

    def set_name(self, name) -> None:
        self.name = name

    def borrow_book(self, book: Book) -> None:
        if book.take_book():
            self.borrowed_books.append(book)

    def return_book(self, book: Book) -> None:
        for i in range(len(self.borrowed_books)):
            if self.borrowed_books[i].get_title() == book.get_title():
                book.return_book()
                del self.borrowed_books[i]
                break


class Library:
    def __init__(self) -> None:
        self.list_of_books = []
        self.list_of_members = []

    def add_book(self, book: Book) -> None:
        # to avoid duplicates, check if book exists

        self.list_of_books.append(book)

    def add_member(self, member: Member) -> None:
        # to avoid duplicates, check if member exists

        self.list_of_members.append(member)

    def print_books(self) -> None:
        for book in self.list_of_books:
            print(book.title)


library = Library()
book1 = Book("title", "author", "123", 2)
book2 = Book("title2", "author2", "1234", 3)
library.add_book(book1)
library.add_book(book2)
library.print_books()
member1 = Member("a", 1)

member1.borrow_book(book1)
print(book1.get_copies())
print(member1.borrowed_books[0].title)
member1.return_book(book1)
print(book1.get_copies())
