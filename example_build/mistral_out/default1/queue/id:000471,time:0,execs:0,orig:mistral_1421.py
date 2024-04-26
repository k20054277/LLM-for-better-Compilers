
# Base class with invariant condition
class Shape:
    def __init__(self, data):
        assert isinstance(data, (list, tuple)) and all(isinstance(i, (int, float)) for i in data), "Data must be a list or tuple of numbers"
        self.data = data

    # Polymorphic method
    def area(self):
        raise NotImplementedError("area method must be implemented in derived classes")

# Derived classes
class Circle(Shape):
    def __init__(self, radius):
        super().__init__([radius])

    def area(self):
        return math.pi * self.data[0] ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__([width, height])

    def area(self):
        return self.data[0] * self.data[1]

if __name__ == "__main__":
    shapes = [Circle(5), Circle(3), Rectangle(4, 6)]

    for shape in shapes:
        print(f"Area of shape: {shape.area()}")
