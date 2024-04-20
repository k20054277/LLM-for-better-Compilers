class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height
    
    @assert
    def assert_positive_values(self, values):
        for value in values:
            assert value > 0, "Values must be positive"
    
rectangle = Rectangle(-1, -2)
try:
    rectangle.assert_positive_values([rectangle.width, rectangle.height])
except AssertionError as error:
    print(error)