
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_area(self):
        return self._width * self._height

    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"

# Usage
rectangle = Rectangle(3, 4)
print(rectangle.get_area())
print(rectangle)
