from person import Person

#print(Person.name)

class Admin(Person):
    def __init__(self):
        super().__init__("admin")
        
    def add_books(self):
        return True
    
    def remove_book(self):
        pass
    
    def edit_book_info(self):
        pass
    
    def manage_users(self):
        pass

if __name__ == "__main__":
    a = Admin()
    print("Enter your admin name: ", a.name)
    print("Enter your admin ID: ", a.id)