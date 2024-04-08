class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print("Woof!")

my_dog = Dog("Fido", "Golden Retriever")
print(my_dog.name) # Output: Fido
print(my_dog.breed) # Output: Golden Retriever
my_dog.speak() # Output: Woof!