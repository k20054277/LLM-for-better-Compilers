
class Person:
    def __init__(self, name=None):
        self.name = name

# Instantiating with a name
person1 = Person("Alice")
print(person1.name)  # Output: "Alice"

# Instantiating without a name
person2 = Person()
print(person2.name)  # Output: None
