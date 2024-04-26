
# Assign values with alias names using as keyword
import math

a = 5.0
b = 3.0

square_root_a = math.sqrt(a) as sqrt_a
cubic_root_b = math.pow(b, 1/3) as cubic_root_b

print("Square root of a: ", sqrt_a)
print("Cubic root of b: ", cubic_root_b)

# Perform mathematical operations using the aliased names
result = sqrt_a + cubic_root_b * a

print("Result: ", result)
