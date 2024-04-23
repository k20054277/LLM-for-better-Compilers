
# Define a simple Person class with name and age attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Function to calculate the hash value of a person object
def person_hash(person):
    return hash((type(person), person.name, person.age))

# Create some Person objects
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Test the assert statement for checking if two persons have the same name and age
def test_persons():
    assert person1.name == "Alice" and person1.age == 30, \
        f"Person1 has name '{person1.name}' and age {person1.age} which is not correct."
    assert person2.name == "Bob" and person2.age == 25, \
        f"Person2 has name '{person2.name}' and age {person2.age} which is not correct."

# Test the hash function for generating unique identifiers for Person objects
def test_hash():
    assert person_hash(person1) == hash((type(Person), "Alice", 30)), \
        "Person1's hash value is not as expected."
    assert person_hash(person2) == hash((type(Person), "Bob", 25)), \
        "Person2's hash value is not as expected."

# Call the test functions
try:
    test_persons()
    test_hash()
    print("All tests passed.")
except AssertionError as e:
    print(f"Test failed: {e}")
