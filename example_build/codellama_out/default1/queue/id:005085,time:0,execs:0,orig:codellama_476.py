# Define a class with two attributes, x and y
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# Create an instance of the Point class
p = Point()

# Set the value of x to 1 using setattr
setattr(p, 'x', 1)

# Print the value of x
print(p.x) # Output: 1

# Set the value of y to None using setattr
setattr(p, 'y', None)

# Print the value of y
print(p.y) # Output: None