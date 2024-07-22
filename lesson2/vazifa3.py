class Person:
    def __init__(self, firstname, lastname, age, phone) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.phone = phone
    
    def info(self):
        print("First Name:", self.firstname)
        print("Last Name:", self.lastname)
        print("Age:", self.age)
        print("Phone:", self.phone)


person = Person("Bobur", "Xalilov", "30" , "Iphone 15 pro")

person.info()