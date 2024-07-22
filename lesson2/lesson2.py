# OOP = object Oriented Programming

class User:
    name = "Olim"
    last_name = "Olimov"
    
    def __init__(self,name,Last_name) -> None:     #dunder metod
        self.name=name
        self.last_name=Last_name
        
    def user_info(self):
        print(f"Name: {self.name} \nLast name: {self.last_name}")
    

bobur=User(name="Bobur", Last_name="Xalilov")    
user=User(name="Sardor", Last_name="xasanov")     

User.user_info(bobur)  
bobur.user_info()      

# print(user.name)
# print(user.last_name)



