class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print("Hello, my name is", self.name)

john = Person("John")
mary = Person("Mary")

if john and mary:
    print("Both John and Mary are present.")
else:
    print("One or both of John and Mary are absent.")