from person import Person

#print(Person.name)

class Admin(Person):
    def __init__(self):
        super().__init__()
        
    def add_books(self):
        return True
    
    def remove_book(self):
        pass
    
    def edit_book_info(self):
        pass
    
    def manage_users(self):
        pass
    
a = Admin()
print("Enter your name(for admin): ", a.name)
print("Enter your ID(admin ID): ", a.id)