
class Rectangle:
    def __init__(self, width, height):
        # Encapsulation: width and height are private attributes
        self._width = width
        self._height = height

    def get_area(self):
        assert self._width > 0, "Invalid width: width should be positive"
        assert self._height > 0, "Invalid height: height should be positive"
        return self._width * self._height

if __name__ == "__main__":
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
    
    # Create a Rectangle instance with provided dimensions
    my_rectangle = Rectangle(width, height)

    # Get and print the area of the rectangle
    print(f"The area of the rectangle is: {my_rectangle.get_area()}")
