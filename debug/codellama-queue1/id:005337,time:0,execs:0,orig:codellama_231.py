class Animal:
  def __init__(self, name):
    self.name = name

  def make_sound(self):
    print("The", self.name, "says 'Roooaaaawwww'")

class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name)
    self.breed = breed

  def make_sound(self):
    print("The", self.name, "says 'Woof woof'")

dog = Dog("Buddy", "Golden Retriever")
dog.make_sound() # Output: The Buddy says 'Woof woof'