class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("Woof!")
    
    def is_adoptable(self):
        return True  # This method always returns True

dog1 = Dog("Fido", 3)
print(dog1.is_adoptable())  # Output: True