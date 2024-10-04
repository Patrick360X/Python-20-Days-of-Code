class Library:
    def __init__(self):
        self.noBooks = 0
        self.Books = []

    def addBooks(self, book):
        self.Books.append(book)
        self.noBooks = len(self.Books)
    
    def booksLibrary(self):
        print(f"This Library has {self.noBooks} books")
        print(f"And there name is:\n{self.Books}")

l1 = Library()
l1.addBooks('Alvin and the chipmunks')
l1.addBooks('Sacred Games')
l1.booksLibrary()