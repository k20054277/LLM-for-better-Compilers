class Person:
    def __init__(self, name):
        self.name = name

    def is_adult(self):
        return self.age >= 18

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be non-negative")
        self._age = value

person1 = Person("Alice")
person1.age = 25
print(person1.is_adult()) # True

person2 = Person("Bob")
person2.age = -1
try:
    print(person2.is_adult())
except ValueError as e:
    print(e)