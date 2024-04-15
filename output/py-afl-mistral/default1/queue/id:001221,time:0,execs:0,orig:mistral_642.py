
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.is_valid = True

    def area(self):
        return self.width * self.height

    def is_valid(self):
        """Return the validity status of the rectangle"""
        return self.is_valid

# Create some rectangles
r1 = Rectangle(2, 3)
r2 = Rectangle(-1, 5)

# Check if the first rectangle is valid
print(f"Rectangle r1 is valid: {r1.is_valid}")

# Set the validity of the second rectangle to False
r2.is_valid = False

# Check if the rectangles' validities
print("Rectangle r1 is valid:", r1.is_valid)
print("Rectangle r2 is valid:", r2.is_valid)
