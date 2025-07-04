from admin import Admin
from user import User
import json

def authenticate_user():
    """Authenticate existing user or register new user"""
    print("\n=== Library Management System ===")
    print("1. Login as existing user")
    print("2. Register as new user")
    
    choice = input("Choose option (1-2): ")
    
    if choice == "1":
        return login_existing_user()
    elif choice == "2":
        return register_new_user()
    else:
        print("Invalid choice.")
        return None

def login_existing_user():
    """Login with existing credentials"""
    user_id = input("Enter your ID: ")
    
    try:
        with open("persons.json", "r") as f:
            persons = json.load(f)
        
        for person in persons:
            if person["id"] == user_id:
                print(f"Welcome back, {person['name']}!")
                if person["role"] == "admin":
                    return Admin(person["name"], person["id"])
                else:
                    return User(person["name"], person["id"])
        
        print("User ID not found.")
        return None
    
    except FileNotFoundError:
        print("No users registered yet.")
        return None

def register_new_user():
    """Register a new user"""
    print("1. Register as Admin")
    print("2. Register as User")
    
    choice = input("Choose role (1-2): ")
    
    if choice == "1":
        return Admin()
    elif choice == "2":
        return User()
    else:
        print("Invalid choice.")
        return None

def main():
    """Main application loop"""
    print("Welcome to Library Management System!")
    
    while True:
        user = authenticate_user()
        
        if user:
            if isinstance(user, Admin):
                user.admin_menu()
            elif isinstance(user, User):
                user.user_menu()
        
        continue_choice = input("\nDo you want to continue? (y/n): ").lower()
        if continue_choice != 'y':
            print("Thank you for using Library Management System!")
            break

if __name__ == "__main__":
    main()