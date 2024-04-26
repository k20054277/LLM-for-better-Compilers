
# Define a custom class named 'Person' with two attributes: name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # A method to check if a person is eligible to vote (18 years or older)
    def is_eligible_to_vote(self):
        return self.age >= 18

# Create instances of 'Person' class with given names and ages
person1 = Person("John Doe", 25)
person2 = Person("Jane Smith", 30)

# Check if each person is eligible to vote or not using 'is_eligible_to_vote()' method
print(f"{person1.name} is eligible to vote: {person1.is_eligible_to_vote()}")  # False
print(f"{person2.name} is eligible to vote: {person2.is_eligible_to_vote()}")  # True

# Using 'True' boolean value in Python
# You can compare variables or expressions to return a boolean (True/False) value
print(5 > 3)       # Output: True
print("apple" < "banana")   # Output: False
