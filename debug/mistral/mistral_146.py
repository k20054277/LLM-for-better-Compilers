
class Animal:
    def __init__(self):
        self.name = ""
    
    def can_fly(self):
        return False

class Bird(Animal):
    def __init__(self, name, wings_length):
        super().__init__()
        self.name = name
        self.wings_length = wings_length

    def can_fly(self):
        return True

# Create an instance of Animal and Bird classes
animal = Animal()
bird = Bird("Eagle", 1.5)

# Testing the methods
print(f"Animal {animal.name} can fly: {animal.can_fly()}")
print(f"Bird {bird.name} can fly: {bird.can_fly()}")
