class Book:
    TYPES = ("Hardcover", "Paperback")
    
    def __init__(self, name, book_type, weight):
        self.name = name,
        self.book_type = book_type,
        self.weight = weight
        
    def __repr__(self):
        """Esto representa un objeto de forma legible para programadores.
           Si fuera para usuarios se usaria el __str__() 
        """
        return f"Book({self.name}, {self.book_type}, weighing {self.weight}g)"
    
    # los classmethod se utilizaron aquí para añadir el hardCover llamando al metodo
    # y luego retornando un nuevo objeto pero con el hardcover o paperback incluido.
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)
    
book = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 600)
    
    
print(book)
print(light)