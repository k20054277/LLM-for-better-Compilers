
# Function that returns a pair of x and y values
def polar_to_cartesian(angle_in_degrees):
    import math
    radius = 100
    x = radius * math.cos(math.radians(angle_in_degrees))
    y = radius * math.sin(math.radians(angle_in_degrees))
    return x, y

# Use as keyword to assign names to the returned values
x, y = polar_to_cartesian(30) as (x_val, y_val)
print("x =", x_val)  # Output: x = 80.96751925476336
print("y =", y_val)  # Output: y = -58.1125159351651
