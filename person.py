import json

class Person():
    def __init__(self, role):
        self.name = input(f"Enter your name ({role}): ")
        self.id = input(f"Enter your ID ({role}): ")
        self.role = role
        
        # only users have borrowed_books
        if self.role == "user":
            self.borrowed_books = []
        self.save_person()
    
    def to_dict(self):
        data = {
            "name": self.name,
            "id": self.id,
            "role": self.role
        }
        if self.role == "user":
            data["borrowed_books"] = self.borrowed_books
        return data

    def save_person(self):
        try:
            with open("persons.json","r") as file:
                persons = json.load(file)
        except FileNotFoundError:
            persons = []
        
        if any(person["id"] == self.id for person in persons):
            return
            
        persons.append(self.to_dict())
        
        with open("persons.json", "w") as file:
            json.dump(persons, file, indent=4)
        
    def view_books(self):
        from book import Book
        Book.view_all_books()

# if __name__ == "__main__":
#     p = Person(input("Who are you(admin/user)?: "))
#     print("Name of the person is: ", p.name)
#     print("Person ID is: ", p.id)
#     print("Person role is: ", p.role)