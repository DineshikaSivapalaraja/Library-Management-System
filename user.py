from person import Person
# import Person from person


class User(Person):
    # isBorrowed = True
    def __init__(self):
        super().__init__() # Call the constructor of the Person class
        # self.isBorrowed = True
        
    def borrow_book(self):
        borrow = input("Did you Borrow book?: ")
        return borrow
    
    def return_book(self):
        # p=Person()
        # print(p.name)
        # return 'yes'
        returnBook = input("Did you return Book?: ")
        #return returnBook
    
    def view_borrowed_book(self):
        return 'yes'


#print(person.name)

u = User()
print("Enter your name(user): ", u.name)
print("Enter your ID(user ID): ", u.id)
# The code snippet is creating an instance of the `User` class and calling the `isBorrowBook()` and
# `returnBook()` methods on that instance.
print("Did you borrow book?: ", u.borrow_book())
#print(u.isBorrowBook())
print("Return book?: ", u.return_book())
#print(u.returnBook())