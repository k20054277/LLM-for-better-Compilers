
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    @staticmethod
    def assert_is_animal(obj):
        if not isinstance(obj, (Animal)):
            msg = f"{type(obj).__name__} is not an Animal instance."
            raise TypeError(msg)

    def make_sound(self):
        self.assert_is_animal(self)
        assert self.sound, "An animal must have a sound."
        print(f"{self.name} says '{self.sound}'")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof!")

if __name__ == "__main__":
    my_dog = Dog("Fido")
    my_dog.make_sound()
