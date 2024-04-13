class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(dog)

# Check if dog is an instance of both Animal and Dog
if issubclass(dog, Animal) and isinstance(dog, Dog):
    print("dog is an instance of both Animal and Dog")