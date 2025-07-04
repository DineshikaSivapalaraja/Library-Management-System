from person import Person
import json

class User(Person):
    # isBorrowed = True
    def __init__(self, name=None, user_id=None):
        if name and user_id:
            self.name = name
            self.id = user_id
            self.role = "user"
            self.borrowed_books = []
        else:
            super().__init__("user") 
        
    def borrow_book(self):
        print("Borrowing a book...")
        book_id = input("Enter Book ID to borrow: ")
        
        # load books
        try:
            with open("book.json", "r") as f:
                books = json.load(f)
        except FileNotFoundError:
            print("No books available.")
            return
        
        #find and check book availability
        book_found = None
        for book in books:
            if book["book_id"] == book_id:
                book_found = book
                break
        
        if not book_found:
            print("Book not found.")
            return
        
        if not book_found.get("available", True):
            print("Book is already borrowed.")
            return
        
        # update book availability
        book_found["available"] = False
        
        # update user's borrowed books
        try:
            with open("persons.json", "r") as f:
                persons = json.load(f)
        except FileNotFoundError:
            print("User data not found.")
            return
        
        for person in persons:
            if person["id"] == self.id and person["role"] == "user":
                if "borrowed_books" not in person:
                    person["borrowed_books"] = []
                person["borrowed_books"].append(book_id)
                break
        
        # save files
        with open("book.json", "w") as f:
            json.dump(books, f, indent=4)
        with open("persons.json", "w") as f:
            json.dump(persons, f, indent=4)
        
        print(f"Book '{book_found['name']}' borrowed successfully!")
    
    def return_book(self):
        print("Returning a book...")
        book_id = input("Enter Book ID to return: ")

        # load persons
        try:
            with open("persons.json", "r") as f:
                persons = json.load(f)
        except FileNotFoundError:
            print("User data not found.")
            
        # find user and check if book is borrowed
        user_found = None
        for person in persons:
            if person["id"] == self.id and person["role"] == "user":
                user_found = person
                break
        
        if not user_found or book_id not in user_found.get("borrowed_books", []):
            print("You haven't borrowed this book.")
            return
        
        # remove from user's borrowed books
        user_found["borrowed_books"].remove(book_id)
        
        # update book availability
        try:
            with open("book.json", "r") as f:
                books = json.load(f)
            
            for book in books:
                if book["book_id"] == book_id:
                    book["available"] = True
                    break
            
            # save files
            with open("book.json", "w") as f:
                json.dump(books, f, indent=4)
            with open("persons.json", "w") as f:
                json.dump(persons, f, indent=4)
            
            print("Book returned successfully!")
        except FileNotFoundError:
            print("Book data not found.")

    def view_borrowed_books(self):
        print("Viewing borrowed books...")
        try:
            with open("persons.json", "r") as f:
                persons = json.load(f)
            
            user_found = None
            for person in persons:
                if person["id"] == self.id and person["role"] == "user":
                    user_found = person
                    break
                
            if not user_found or not user_found.get("borrowed_books"):
                print("You have no borrowed books.")
                return
            
            # load book details
            with open("book.json", "r") as f:
                books = json.load(f)
                
            for book_id in user_found["borrowed_books"]:
                for book in books:
                    if book["book_id"] == book_id:
                        print(f"- {book['name']} by {book['author']} (ID: {book_id})")
                        break
        
        except FileNotFoundError:
            print("No data found.")
    
    def user_menu(self):
        while True:
            print(f"\n=== User Menu - Welcome {self.name} ===")
            print("1. View All Books")
            print("2. Borrow Book")
            print("3. Return Book")
            print("4. View My Borrowed Books")
            print("5. Logout")
            
            choice = input("Choose option (1-5): ")
            
            if choice == "1":
                from book import Book
                Book.view_all_books()
            elif choice == "2":
                self.borrow_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.view_borrowed_books()
            elif choice == "5":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     u = User()
#     u.user_menu()
#     # print("Enter your username: ", u.name)
#     # print("Enter your user ID: ", u.id)
#     # print("Did you borrow book?: ", u.borrow_book())
#     # print("Return book?: ", u.return_book())