
# Defining a base class and a derived class
class BaseShape:
    def area(self):
        pass
    
class Rectangle(BaseShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Creating an instance of the derived class
rectangle = Rectangle(5, 10)

# Using isinstance() to check the type of an object
if isinstance(rectangle, BaseShape):
    print("The rectangle is a BaseShape")
else:
    print("The rectangle is not a BaseShape")

# Using as to assign the result of a function call to a variable
as_base_shape = as_value(isinstance(rectangle, BaseShape))

if type(as_base_shape) is True:
    print("The as_base_shape variable holds a Boolean value representing True")
else:
    print("An error occurred")

# A helper function to simplify the use of isinstance() with as
def as_value(condition):
    return condition if type(condition) is bool else (bool(condition) and condition)
