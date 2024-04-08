import asyncio
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    async def make_sound(self):
        print("Bark!")

class Cat(Animal):
    async def make_sound(self):
        print("Meow!")

async def main():
    dog = Dog()
    cat = Cat()

    # Check if `Dog` is a subclass of `Animal`
    print(issubclass(Dog, Animal))  # Output: True

    # Check if `Cat` is a subclass of `Animal`
    print(issubclass(Cat, Animal))  # Output: True

    # Call the `make_sound` method on each instance using `await`
    await dog.make_sound()  # Output: Bark!
    await cat.make_sound()  # Output: Meow!

asyncio.run(main())