
# Animal base class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("This animal makes a sound.")


# Cat class inherits from Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # call the parent constructor (Animal) using `super()` and `as`
        self.color = color

    def make_sound(self):
        print(f"{self.name} is a cat and makes a meowing sound: meow!")


# Dog class also inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # call the parent constructor (Animal) using `super()` and `as`
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} is a dog and makes a barking sound: wooof!")


# Instantiate and call methods for cat and dog objects
cat = Cat("Mittens", "gray")
cat.make_sound()

dog = Dog("Fido", "Labrador")
dog.make_sound()
