
class Person:
    def __init__(self, age, is_employed):
        self.age = age
        self.is_employed = is_employed

    def is_valid(self):
        return self.age > 18 and self.is_employed

# Create instances of Person class
person1 = Person(25, True)
person2 = Person(17, False)

print("Person 1 is valid:", person1.is_valid()) # Prints: Person 1 is valid: True
print("Person 2 is valid:", person2.is_valid()) # Prints: Person 2 is valid: False

# Using and operator directly with attributes
print("Person 1 is valid using and operator:", (person1.age > 18) and person1.is_employed) # Prints: Person 1 is valid using and operator: True
