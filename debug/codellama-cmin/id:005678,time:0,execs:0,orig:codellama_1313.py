# Import the necessary modules
from typing import TypeVar, Generic, Any

# Define a type variable for the class hierarchy
T = TypeVar('T')

# Define a base class
class Animal:
    pass

# Define a subclass of Animal
class Dog(Animal):
    def bark(self) -> None:
        print("Woof!")

# Use assert to check that an object is an instance of a specific class
def test_assert(animal: T) -> bool:
    assert isinstance(animal, Dog), "The animal must be an instance of Dog"
    return True

# Use issubclass to check if a class is a subclass of another class
def test_issubclass(dog: Dog) -> bool:
    assert issubclass(dog.__class__, Animal), "The dog class must be a subclass of Animal"
    return True