from person import Person
# import Person from person


class User(Person):
    # isBorrowed = True
    def __init__(self):
        super().__init__("user") # Call the constructor of the Person class
        
    def borrow_book(self):
        borrow = input("Did you Borrow book?: ")
        return borrow
    
    def return_book(self):
        returnBook = input("Did you return Book?: ")
        return returnBook
    
    def view_borrowed_book(self):
        return 'yes'


#print(person.name)
if __name__ == "__main__":
    u = User()
    print("Enter your username: ", u.name)
    print("Enter your user ID: ", u.id)
    print("Did you borrow book?: ", u.borrow_book())
    print("Return book?: ", u.return_book())