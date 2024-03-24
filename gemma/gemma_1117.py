
# Demonstrating the use of as and dir

# Define a class called Person
class Person:
    name = "John Doe"
    age = 30

# Create an instance of the Person class
person = Person()

# Use as to bind the instance to the person variable
as person

# Print the attributes of the person object
print(dir(person))

# Output: ['__doc__', '__dict__', '__docclass__', 'age', 'name']

# Print the name and age of the person
print("Name:", person.name)
print("Age:", person.age)

# Output:
# Name: John Doe
# Age: 30
