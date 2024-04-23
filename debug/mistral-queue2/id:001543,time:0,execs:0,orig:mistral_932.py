
# Define base classes
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Create instances of subclasses
dog = Dog("Fido", "Brown")
cat = Cat("Whiskers", "White")

# Demonstrate usage of and operator
if dog.color == "Brown" and dog.make_sound() == "Woof!":
    print(f"{dog.name} is a dog and barks 'Woof!'")
else:
    print("Invalid dog instance")

if cat.color == "White" and cat.make_sound() == "Meow!":
    print(f"{cat.name} is a cat and meows 'Meow'")
else:
    print("Invalid cat instance")
