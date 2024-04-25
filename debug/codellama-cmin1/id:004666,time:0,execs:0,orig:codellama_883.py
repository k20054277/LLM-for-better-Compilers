# Using and property

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def full_name(self):
        return f"{self.name} {self.age}"

p = Person("Alice", 30)
print(p.full_name)