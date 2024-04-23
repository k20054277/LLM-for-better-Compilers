class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

dog = Dog("Max")
cat = Cat("Whiskers")

# Using as
print(dog.name)  # Output: Max
print(cat.name)  # Output: Whiskers

# Using isinstance
if isinstance(dog, Animal):
    print("Dog is an instance of Animal")
if isinstance(cat, Animal):
    print("Cat is an instance of Animal")
if isinstance(dog, Dog):
    print("Dog is an instance of Dog")
if isinstance(cat, Cat):
    print("Cat is an instance of Cat")