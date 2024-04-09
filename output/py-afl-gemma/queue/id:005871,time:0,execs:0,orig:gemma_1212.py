
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, " + self.name)

class Child(Parent):
    def __init__(self, name, age, hobbies):
        super().__init__(name, age)
        self.hobbies = hobbies

    def list_hobbies(self):
        print("My hobbies are:")
        for hobby in self.hobbies:
            print(hobby)

# Create an instance of the Child class
child = Child("John", 20, ["reading", "music", "sports"])

# Call the say_hello method
child.say_hello()

# Call the list_hobbies method
child.list_hobbies()
