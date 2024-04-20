class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal says " + self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("Woof!")

dog = Dog("Fido", "Poodle")
assert dog.name == "Fido"
assert dog.breed == "Poodle"
dog.speak()