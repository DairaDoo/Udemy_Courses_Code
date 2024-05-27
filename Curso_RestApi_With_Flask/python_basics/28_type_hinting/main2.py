class Book:
    TYPES = ("hardcover", "paperback")
    
    
    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name,
        self.book_type = book_type,
        self.weight = weight
    
    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"
    
    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":  # se usan comillas al refeirse a un objeto si mi metodo pertenece a esa clase. 
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)
    
book1 = Book.hardcover("Harry Potter", 1500)
book2 = Book.paperback("gokuBook", 500)
print(book1)
print(book2)