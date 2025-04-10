import json
class Book:
    def __init__(self, name, book_id, author, no_of_pages, year):
        self.name = name
        self.book_id = book_id
        self.author = author
        self.no_of_pages = no_of_pages
        self.year = year
        #self.save_Book()
    
    def isBorrowed(self):
        pass
    
    def to_dict(self):
        return {
            "name": self.name,
            "book_id": self.book_id,
            "author": self.author,
            "no_of_pages": self.no_of_pages,
            "year": self.year
        }
    
    def save_book(self):
        try:
            with open("book.json", "r") as file:
                books = json.load(file)
        except FileNotFoundError:
            books = []
        
        # for book in books:
        #     if book["book_id"] == self.book_id : 
        if any(book["book_id"] == self.book_id for book in books):
            print(f"Book with ID '{self.book_id}' already exists. Skipping save.")
            return
            
        books.append(self.to_dict())
        
        with open("book.json", "w") as file:
            json.dump(books, file, indent=4)

if __name__ == "__main__":
    name = input("Enter the name of the book: " )
    book_id = input("Enter the book ID: ")
    author = input("Enter the Author name of the book: ")
    no_of_pages = int(input("Enter the number of pages: "))
    year = int(input("Enter published year: "))

    b = Book(name,book_id,author, no_of_pages, year)
    # print(b.isBorrowed())
    print(b.name)
    print(b.save_book())
        
        
