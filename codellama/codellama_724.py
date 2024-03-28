class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am a animal.")

class Dog(Animal):
    def speak(self):
        print("Arf! Arf!")

class Cat(Animal):
    def speak(self):
        print("Meow! Meow!")

dog = Dog("Fido")
cat = Cat("Whiskers")

print(dog.name)  # Output: Fido
print(cat.name)  # Output: Whiskers

dog.speak()  # Output: Arf! Arf!
cat.speak()   # Output: Meow! Meow!