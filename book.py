import json

class Book:
    def __init__(self, name, book_id, author, no_of_pages, year, available=True):
        self.name = name
        self.book_id = book_id
        self.author = author
        self.no_of_pages = no_of_pages
        self.year = year
        self.available = available
    
    def to_dict(self):
        return {
            "name": self.name,
            "book_id": self.book_id,
            "author": self.author,
            "no_of_pages": self.no_of_pages,
            "year": self.year,
            "available": self.available
        }
    
    def save_book(self):
        try:
            with open("book.json", "r") as file:
                books = json.load(file)
        except FileNotFoundError:
            books = []
        
        if any(book["book_id"] == self.book_id for book in books):
            print(f"Book with ID '{self.book_id}' already exists. Skipping save.")
            return
            
        books.append(self.to_dict())
        
        with open("book.json", "w") as file:
            json.dump(books, file, indent=4)
        print("Book saved successfully!")

    def load_books():
        try:
            with open("book.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save_books(books):
        with open("book.json", "w") as f:
            json.dump(books, f, indent=4)
    
    def add_book():
        print("\n=== Adding New Book ===")
        name = input("Book name: ")
        book_id = input("Book ID: ")
        author = input("Author: ")
        no_of_pages = int(input("Number of pages: "))
        year = int(input("Year: "))
        
        books = Book.load_books()
        if any(book["book_id"] == book_id for book in books):
            print("Book ID already exists.")
            return
        
        new_book = Book(name, book_id, author, no_of_pages, year)
        books.append(new_book.to_dict())
        Book.save_books(books)
        print("Book added successfully!")
    
    def remove_book(book_id):
        books = Book.load_books()
        original_count = len(books)
        books = [book for book in books if book["book_id"] != book_id]
        
        if len(books) < original_count:
            Book.save_books(books)
            print("Book removed successfully!")
        else:
            print("Book not found.")
    
    def edit_book(book_id):
        books = Book.load_books()
        
        for book in books:
            if book["book_id"] == book_id:
                print(f"\nEditing book: {book['name']}")
                book["name"] = input(f"New name [{book['name']}]: ") or book["name"]
                book["author"] = input(f"New author [{book['author']}]: ") or book["author"]
                pages_input = input(f"New pages [{book['no_of_pages']}]: ")
                if pages_input:
                    book["no_of_pages"] = int(pages_input)
                year_input = input(f"New year [{book['year']}]: ")
                if year_input:
                    book["year"] = int(year_input)
                
                Book.save_books(books)
                print("Book updated successfully!")
                return
        
        print("Book not found.")
    
    def view_all_books():
        print("\n=== All Books ===")
        books = Book.load_books()
        if books:
            for book in books:
                status = "Available" if book.get("available", True) else "Borrowed"
                print(f"'{book['name']}' by {book['author']} (ID: {book['book_id']}) - {status}")
        else:
            print("No books in library.")

# if __name__ == "__main__":
#     name = input("Enter the name of the book: ")
#     book_id = input("Enter the book ID: ")
#     author = input("Enter the Author name of the book: ")
#     no_of_pages = int(input("Enter the number of pages: "))
#     year = int(input("Enter published year: "))

#     b = Book(name, book_id, author, no_of_pages, year)
#     print(f"Book name: {b.name}")
#     b.save_book()
