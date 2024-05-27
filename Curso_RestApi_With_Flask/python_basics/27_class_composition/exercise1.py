class BookShelf():
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."
    
shelf = BookShelf(300)


class Book(BookShelf):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Book {self.name}"
    
book1 = Book("Harry Potter")
book2 = Book("Harry Peter")
shelf = BookShelf(book1, book2)
print(shelf)

        
        