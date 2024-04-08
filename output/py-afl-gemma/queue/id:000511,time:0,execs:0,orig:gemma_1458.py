
# Define a base class called Animal
class Animal:
    def make_sound(self):
        print("The animal makes a sound")

# Define a subclass called Dog that inherits from Animal
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Define a subclass called Cat that inherits from Animal
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Create instances of the different subclasses
dog = Dog()
cat = Cat()

# Assert that the make_sound method works as expected
assert dog.make_sound() == "Woof!"
assert cat.make_sound() == "Meow!"

# Print the sounds of the dog and cat
dog.make_sound()
cat.make_sound()
