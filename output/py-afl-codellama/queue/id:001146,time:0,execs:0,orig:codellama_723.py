class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("The animal says: " + self.name)

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def speak(self):
        print("Woof!")

dog = Dog("Buddy", 3)
dog.speak() # Output: Woof!