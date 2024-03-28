
# Base class with a method
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_sound(self):
        print("The animal makes a sound")

# Derived class 1 that overrides the method from the base class
class Dog(Animal):
    def __init__(self, name, color, breed):
        super().__init__(name, color)
        self.breed = breed

    def make_sound(self):
        print("The dog says: Woof!")

# Derived class 2 that also overrides the method from the base class
class Cat(Animal):
    def __init__(self, name, color, breed=None):
        super().__init__(name, color)
        self.breed = breed if breed else "unknown"

    def make_sound(self):
        print("The cat says: Meow!")

# Instantiating derived classes and calling methods
dog = Dog("Rex", "brown", "Labrador")
cat = Cat("Whiskers", "gray")

# Using and to combine conditions
print(dog.color == "brown" and dog.breed != None)  # This will print: True
print(cat.color == "gray" and cat.breed is not None)  # This will print: True

# Calling make_sound method on instances
dog.make_sound()
cat.make_sound()
