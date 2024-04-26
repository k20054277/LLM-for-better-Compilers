
# Define a base class called Animal
class Animal:
    def speak(self):
        print("The animal speaks")

# Define a subclass called Dog that inherits from Animal
class Dog(Animal):
    def speak(self):
        print("Woof!")

# Define a subclass called Cat that inherits from Animal
class Cat(Animal):
    def speak(self):
        print("Meow!")

# Create instances of the different subclasses
dog = Dog()
cat = Cat()

# Call the speak method on each instance
dog.speak()
cat.speak()

# Output:
# The animal speaks
# Woof!
# Meow!
