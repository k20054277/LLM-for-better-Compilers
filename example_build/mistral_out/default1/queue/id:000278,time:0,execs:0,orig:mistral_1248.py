
# Example using the math module
import math

result = math.pythagorean_iseries(3)  # This function returns a tuple containing two values: a sequence and the sum of its elements
sequence, sum = result
print("Sum:", sum)  # We can access the sum directly

# Using 'as' to assign an alias
result = math.pythagorean_iseries(3)
sequence, sum as total_sum  # Assigns 'sum' the name 'total_sum' for easier reading
print("Total Sum:", total_sum)
