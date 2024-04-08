class Animal:
    def speak(self):
        print("The animal makes a noise.")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!")

class Cat(Animal):
    def speak(self):
        super().speak()
        print("Meow!")

dog = Dog()
cat = Cat()

# Output:
# The animal makes a noise.
# Woof!
# The animal makes a noise.
# Meow!