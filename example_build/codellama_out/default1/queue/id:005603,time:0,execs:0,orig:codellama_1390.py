class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("The animal says...")
    
    def move(self, distance):
        print(f"The animal moved {distance} meters.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def bark(self):
        print("Woof!")

dog = Dog("Buddy", "Golden Retriever")
assert dog.name == "Buddy"
assert dog.breed == "Golden Retriever"
assert isinstance(dog, Animal)

dog.speak()  # Output: The animal says...
dog.move(10)  # Output: The animal moved 10 meters.
dog.bark()    # Output: Woof!