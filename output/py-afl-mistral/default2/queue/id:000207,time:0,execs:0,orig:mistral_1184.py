
import math

x, y = 3, 4
r, theta = math.polar(x, y) # Returns a tuple (r, theta) representing polar coordinates

print("x = {}".format(x))
print("y = {}".format(y))

# Assign r and theta from the polar_coords tuple using as keyword
r, theta as radius, angle 

print("radius = {}".format(radius))
print("angle = {}".format(angle))
