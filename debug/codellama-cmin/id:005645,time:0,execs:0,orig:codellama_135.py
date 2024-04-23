class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("The animal says " + self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def bark(self):
        print("Woof!")
    
    def sound(self):
        super().sound()
        print("The dog says " + self.breed)

my_dog = Dog("Fido", "Golden Retriever")
my_dog.bark()
my_dog.sound()