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
        print("The dog " + self.name + " says " + self.breed)
    
    def sit(self):
        print("The dog sits")

class GoldenRetriever(Dog):
    def __init__(self, name, breed, color):
        super().__init__(name, breed)
        self.color = color
    
    def speak(self):
        print("The golden retriever " + self.name + " says " + self.breed + " and has the color " + self.color)