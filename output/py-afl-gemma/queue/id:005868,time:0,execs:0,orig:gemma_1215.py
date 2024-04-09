
def square(x):
    return x ** 2

# Define a function to calculate the area of a rectangle
def area(width, height):
    return width * height

# Use as to simplify the square function
area_of_square = lambda w, h: area(square(w), h)

# Calculate the area of a square with side length 5
area_of_square(5)  # Output: 25

# Calculate the area of a rectangle with width 4 and height 3
area_of_square(4, 3)  # Output: 12
