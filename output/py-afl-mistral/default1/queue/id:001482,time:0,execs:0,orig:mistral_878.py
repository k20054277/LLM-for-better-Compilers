
# Define a class with some initial attributes
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of the class
obj = MyClass("John Doe", 30)

# Use and to check multiple conditions
if obj.age > 25 and obj.age < 40:
    print("The person is in the desired age range.")

# Use setattr to dynamically set attributes
new_attribute = "greeting"
value = "Hello, I'm {}!".format(obj.name)
setattr(obj, new_attribute, value)

# Access the new attribute using getattr
print(getattr(obj, new_attribute))
