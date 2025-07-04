from person import Person
from book import Book
import json

class Admin(Person):
    def __init__(self, name=None, admin_id=None):
        if name and admin_id:  
            self.name = name
            self.id = admin_id
            self.role = "admin"
        else:
            super().__init__("admin")  

    def add_books(self):
        print("Adding a new book...")
        Book.add_book()
    
    def remove_book(self):
        print("Removing a book...")
        book_id = input("Enter Book ID to remove: ")
        Book.remove_book(book_id)

    def edit_book_info(self):
        print("Editing book information...")
        book_id = input("Enter Book ID to edit: ")
        Book.edit_book(book_id)
    
    def view_all_users(self):
        try:
            with open("persons.json", "r") as f:
                persons = json.load(f)
            users = [p for p in persons if p["role"] == "user"]
            if users:
                print("\n=== All Users ===")
                for user in users:
                    borrowed = user.get("borrowed_books", [])
                    print(f"Name: {user['name']}, ID: {user['id']}, Borrowed Books: {len(borrowed)}")
            else:
                print("No users found.")
        except FileNotFoundError:
            print("No users found.")

    def manage_users(self):
        print("\n=== Managing Users ===")
        print("1. View all users")
        print("2. Remove user")
        choice = input("Choose option: ")
        
        if choice == "1":
            self.view_all_users()
        elif choice == "2":
            user_id = input("Enter User ID to remove: ")
            self.remove_user(user_id)
            
    def remove_user(self, user_id):
        try:
            with open("persons.json", "r") as f:
                persons = json.load(f)
            original_count = len(persons)
            persons = [p for p in persons if not (p["id"] == user_id and p["role"] == "user")]
            
            if len(persons) < original_count:
                with open("persons.json", "w") as f:
                    json.dump(persons, f, indent=4)
                print("User removed successfully!")
            else:
                print("User not found.")
        except FileNotFoundError:
            print("No users found.")
    
    def admin_menu(self):
        while True:
            print(f"\n=== Admin Menu - Welcome {self.name} ===")
            print("1. Add Books")
            print("2. Remove Book")
            print("3. Edit Book Info")
            print("4. Manage Users")
            print("5. View All Books")
            print("6. Logout")
            
            choice = input("Choose option (1-6): ")
            
            if choice == "1":
                self.add_books()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.edit_book_info()
            elif choice == "4":
                self.manage_users()
            elif choice == "5":
                Book.view_all_books()
            elif choice == "6":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     a = Admin()
#     a.admin_menu()