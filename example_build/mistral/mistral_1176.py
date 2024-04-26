
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("This animal makes a sound...")

    # Polymorphic method with empty implementation in base class
    def sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("A dog says: Woof!")
        self.sound()  # Calling the sound method of the derived class or base class using 'as' keyword is not possible

    def sound(self):
        print("A dog barks.")

class Bird(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def make_sound(self):
        print("A bird says: Tweet tweet!")
        self.sound()  # Calling the sound method of the derived class or base class using 'as' keyword is not possible

    def sound(self):
        print("A bird chirps.")
