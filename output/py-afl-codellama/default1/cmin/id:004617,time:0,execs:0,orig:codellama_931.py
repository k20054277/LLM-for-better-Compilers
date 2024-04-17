class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def is_adult(self):
        return self.age >= 18 and self.is_old()
    
    def is_old(self):
        return self.age > 65

john = Person("John Doe", 30)
print(john.is_adult()) # False

jane = Person("Jane Doe", 40)
print(jane.is_adult()) # True