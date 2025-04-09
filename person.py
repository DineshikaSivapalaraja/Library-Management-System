class Person():
    def __init__(self):
        self.name = input("Enter your name: ")
        self.id = input("Enter your id: ")
        
    def view_books(self):
        pass


if __name__=="main":
    p = Person()
    print("Name of the person is: ", p.name)
    print("User ID is: ", p.id)
