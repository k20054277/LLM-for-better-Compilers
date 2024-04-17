
class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value >= 0:
            self._width = value
        else:
            raise ValueError("Width must be non-negative")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value >= 0:
            self._height = value
        else:
            raise ValueError("Height must be non-negative")

    def area(self):
        """Return the area of this rectangle"""
        return self.width * self.height

    def __str__(self):
        """Return a string representation of this rectangle"""
        return f"Rectangle({self.width}, {self.height})"

# Create two rectangles and check if their areas are both greater than 10
rectangle1 = Rectangle(2, 5)
rectangle2 = Rectangle(3, 4)

if rectangle1.area() > 10 and rectangle2.area() > 10:
    print("Both rectangles have areas greater than 10")
else:
    print("One or both rectangles do not have areas greater than 10")
