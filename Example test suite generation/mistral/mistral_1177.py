
# Define the Circle class
class Circle:
    # Initialize the circle object with radius as a private attribute using _ as prefix
    def __init__(self, radius):
        self._radius = radius

    # Public method to get the area of the circle
    def get_area(self):
        return 3.14 * (self._radius ** 2)

# Create an instance of Circle with a specified radius and print its area
circle = Circle(5)
area = circle.get_area()
print(f"The area of the circle is: {area}")

# Attempt to access the private attribute _radius directly
# Python does not allow direct access to private attributes
# However, we can create a public method to get the radius if needed
# try:
#     print("Radius: ", circle._radius)
# except AttributeError as e:
#     print(e)
