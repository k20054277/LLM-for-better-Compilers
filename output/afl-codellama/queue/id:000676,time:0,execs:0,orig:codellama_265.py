class Animal(object):
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("The " + self.name + " says meow!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        super().speak()
        print("The cat also likes to purr.")

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())