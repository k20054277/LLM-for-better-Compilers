
import pickle

# Define a class called Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, " + self.name + "!")

# Create a person object
person = Person("John Doe", 30)

# Serialize the person object to a file
with open("person.pkl", "wb") as f:
    pickle.dump(person, f)

# Deserialize the person object from the file
with open("person.pkl", "rb") as f:
    person_recovered = pickle.load(f)

# Print the name and age of the recovered person
print("Name:", person_recovered.name)
print("Age:", person_recovered.age)

# Have the recovered person greet themselves
person_recovered.greet()
