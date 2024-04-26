class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(hasattr(person, "name")) # prints True
print(hasattr(person, "age")) # prints False

setattr(person, "age", 30)
print(hasattr(person, "age")) # prints True