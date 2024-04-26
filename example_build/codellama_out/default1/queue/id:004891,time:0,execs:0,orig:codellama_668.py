class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

if issubclass(Dog, Animal) == True:
    print("Dog is a subclass of Animal")

if issubclass(Cat, Animal) == True:
    print("Cat is a subclass of Animal")