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
        print("The dog says: " + self.name)
        print("I am a " + self.breed)

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def speak(self):
        print("The cat says: " + self.name)
        print("I am a " + self.color)

# create an instance of the Animal class
animal = Animal("Fido")
print(animal.speak())  # prints "The animal says: Fido"

# create an instance of the Dog class
dog = Dog("Rufus", "Golden Retriever")
print(dog.speak())  # prints "The dog says: Rufus" and "I am a Golden Retriever"

# create an instance of the Cat class
cat = Cat("Whiskers", "black")
print(cat.speak())  # prints "The cat says: Whiskers" and "I am a black"