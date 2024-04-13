class Shape:
    def __init__(self, color):
        self.color = color
    
    def draw(self):
        pass
    
    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return self.color

class Circle(Shape):
    def __init__(self, radius, color=None):
        super().__init__(color)
        self.radius = radius
    
    def draw(self):
        print("Drawing a circle with radius", self.radius, "and color", self.color)
    
    def set_radius(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius

class Rectangle(Shape):
    def __init__(self, width, height, color=None):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def draw(self):
        print("Drawing a rectangle with width", self.width, "and height", self.height, "and color", self.color)
    
    def set_width(self, width):
        self.width = width
    
    def get_width(self):
        return self.width
    
    def set_height(self, height):
        self.height = height
    
    def get_height(self):
        return self.height

def test_polymorphism():
    circle = Circle(5, "red")
    rectangle = Rectangle(3, 4, "blue")
    
    assert isinstance(circle, Shape) and isinstance(rectangle, Shape)
    
    print("Circle:", circle.get_color())
    print("Rectangle:", rectangle.get_color())
    
    circle.set_color("green")
    rectangle.set_color("yellow")
    
    assert circle.get_color() == "green" and rectangle.get_color() == "yellow"
    
    print("Circle:", circle.get_color())
    print("Rectangle:", rectangle.get_color())