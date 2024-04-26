
class Animal:
    def __init__(self, name, is_mammal=True):
        self.name = name
        self.is_mammal = is_mammal

    def make_sound(self):
        if self.is_mammal:
            print("{} makes a sound!".format(self.name))
        else:
            raise TypeError("This is not a mammal.")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, False)

class Dog(Animal):
    pass

animal1 = Animal("Lion")
animal1.make_sound() # Lion makes a sound!

animal2 = Bird("Parrot")
animal2.make_sound() # Parrot makes no sound, but it does not raise an error

animal3 = Dog("Rex")
animal3.make_sound() # Rex makes a sound!
