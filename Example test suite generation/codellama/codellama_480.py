class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal says 'Ruff'")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.breed = "Golden Retriever"

    def speak(self):
        print("The dog says 'Woof woof'")

my_dog = Dog("Fido")
print(my_dog.name)  # Output: Fido
print(my_dog.breed)  # Output: Golden Retriever
my_dog.speak()  # Output: The dog says 'Woof woof'