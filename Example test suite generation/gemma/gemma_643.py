
def demonstrate_true_and_getattr(cls):
    print(True)
    print(getattr(cls, 'name'))

# Define a class
class Person:
    name = 'John Doe'

# Create an instance of the class
person = Person()

# Call the demonstrate_true_and_getattr function
demonstrate_true_and_getattr(person)

# Output:
# True
# John Doe
