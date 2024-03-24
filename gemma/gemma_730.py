
# Define a parent class called Animal
class Animal:
    def make_sound(self):
        print("The animal makes a sound.")

# Define a subclass of Animal called Dog
class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Define a subclass of Animal called Cat
class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Create instances of the Dog and Cat classes
dog = Dog()
cat = Cat()

# Call the make_sound method on each instance
dog.make_sound()
cat.make_sound()

# Output:
# Woof!
# Meow!

