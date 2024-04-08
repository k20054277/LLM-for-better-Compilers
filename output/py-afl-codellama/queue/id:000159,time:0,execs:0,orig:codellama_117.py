class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

p1 = Person("Alice", 30)
p2 = Person("Bob", 35)

if p1 and p2:
    print("Both p1 and p2 are non-empty objects.")