
# Base Class
class Shape:
    def area(self):
        pass

# Derived Classes
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Function to calculate the area of a given shape
def calculate_area(shape):
    return shape.area() if callable(shape.area) else None

# Test Cases
circle = Circle(5)
rectangle = Rectangle(4, 6)
shapes = [circle, rectangle]

for shape in shapes:
    area = calculate_area(shape)
    if area is not None:
        print(f'The area of the {type(shape).__name__} is: {area}')
