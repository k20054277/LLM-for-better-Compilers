class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal says: " + self.name)

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("The dog says: " + self.name + " barks!")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        print("The cat says: " + self.name + " meows!")

def demonstrate_inheritance():
    dog1 = Dog("Fido", "Golden Retriever")
    dog2 = Dog("Buddy", "Dachshund")
    cat1 = Cat("Whiskers", "black")
    cat2 = Cat("Fluffy", "gray")

    print(dog1.speak())  # Output: The dog says: Fido barks!
    print(dog2.speak())  # Output: The dog says: Buddy barks!
    print(cat1.speak())  # Output: The cat says: Whiskers meows!
    print(cat2.speak())  # Output: The cat says: Fluffy meows!

if __name__ == "__main__":
    demonstrate_inheritance()