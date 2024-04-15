
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def is_same_person(self, other):
        return type(self) == type(other) and self.age == other.age and self.gender == other.gender

# Create some instances of the Person class
person1 = Person("Alice", 25, "Female")
person2 = Person("Bob", 25, "Male")
person3 = Person("Alice", 25, "Female")

# Check if person1 is the same as person3 using 'is_same_person' method
print(person1.is_same_person(person3))  # Output: True

# Check if person1 is the same as person2
print(person1.is_same_person(person2))  # Output: False
