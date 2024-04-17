class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("The animal makes a sound.")
    
    def move(self):
        print("The animal moves.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def bark(self):
        print("Woof!")

dog = Dog("Fido")
dog.bark()  # Output: Woof!