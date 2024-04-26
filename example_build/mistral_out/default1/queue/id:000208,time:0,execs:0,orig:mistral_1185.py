
# Function to calculate the area of a rectangle or a square
def shape_area(length=1, width=1, is_square=False):
    if is_square:
        length = width
    area = length * width
    print("Area:", area)

# Calling the function with rectangular dimensions (two distinct lengths)
shape_area()
shape_area(3, 4)

# Calling the function with square dimensions (same length and width)
shape_area(5)

# This call is equivalent to shape_area(width=3, length=3)
shape_area(3, 3, True)
