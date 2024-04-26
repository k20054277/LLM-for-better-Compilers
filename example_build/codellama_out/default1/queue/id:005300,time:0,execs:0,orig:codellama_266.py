class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Woof!")

dog = Dog("Fido", "Golden Retriever")
print(dog.name)
print(dog.breed)
dog.make_sound()