
# Import the math module
import math

# Define a function to calculate the area of a circle
def area_of_circle(r):
    # Use the math module to calculate the area of a circle
    area = math.pi * r ** 2
    return area

# Get the radius of a circle from the user
radius = float(input("Enter the radius of a circle: "))

# Calculate the area of the circle
area = area_of_circle(radius)

# Print the area of the circle
print("The area of the circle is:", area)
