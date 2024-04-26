
# Example 1: Renaming a variable using 'as'
import math
x = 5
y = 3
radius = (x**2 + y**2)**0.5
result = math.sqrt(radius)
print("Result:", result)

# Using 'as' to rename 'result' as 'square_root'
square_root = math.sqrt(radius) as root
print("Square Root (alias):", root)
