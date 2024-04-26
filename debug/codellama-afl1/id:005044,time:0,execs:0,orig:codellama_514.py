# Define a class to represent a shape
class Shape:
    def __init__(self, color):
        self.color = color

    # Define an abstract method to calculate the area of the shape
    @abstractmethod
    def area(self):
        pass

# Define a subclass to represent a rectangle
class Rectangle(Shape):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        super().__init__(color)

    # Implement the area method for the rectangle class
    def area(self):
        return self.width * self.height

# Define a subclass to represent a circle
class Circle(Shape):
    def __init__(self, radius, color):
        self.radius = radius
        super().__init__(color)

    # Implement the area method for the circle class
    def area(self):
        return 3.14 * (self.radius ** 2)

# Create a list of shapes
shapes = [Rectangle(5, 7, "red"), Circle(8, "blue")]

# Print the area of each shape in the list
for shape in shapes:
    print("The area of", shape, "is", shape.area())