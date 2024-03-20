class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

# Create a list of animals
animals = [Dog('Fido'), Cat('Whiskers')]

# Use None to represent a missing value
animals.append(None)

# Print the names of all the animals in the list, including the missing value
for animal in animals:
    if animal is not None:
        print(animal.name)