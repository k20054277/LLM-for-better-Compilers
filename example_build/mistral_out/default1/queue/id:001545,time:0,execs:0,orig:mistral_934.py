
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def is_valid(self):
        """Check if a person's name and age are valid"""
        return (type(self._name) is str) and (self._age > 0)

# Usage:
p1 = Person("John Doe", 25)
print(p1.is_valid()) # True
p2 = Person("John", -5)
print(p2.is_valid()) # False
