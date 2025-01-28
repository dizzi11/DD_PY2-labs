class Book:
    def __init__(self, id, name, pages):
        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id={self.id}, name='{self.name}', pages={self.pages})"

class Library:
    def __init__(self, books):
        if books is not None:
            self.books = books
        else:
            ...
    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1
    def get_index_by_book_id(self, id):
        for index, book in enumerate(self.books):
            if book.id == id:
                return index
            else:
                raise ValueError("Книги с таким id не существует")
book1 = Book(id=1, name='Book One', pages=100)
book2 = Book(id=2, name='Book Two', pages=150)
library = Library(books=[book1, book2])
print(library.get_next_book_id())
print(library.get_index_by_book_id(1))
