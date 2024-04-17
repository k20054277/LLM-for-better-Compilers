class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

def polymorphic_method(animal):
    animal.speak()

if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    polymorphic_method(dog)  # Output: Woof!
    polymorphic_method(cat)  # Output: Meow!