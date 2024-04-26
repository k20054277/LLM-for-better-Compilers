
# Function to compute the square root of a number (or return None if the number is negative)
def sqrt(number):
    if number < 0:
        return None
    else:
        import math
        return math.sqrt(number)

# Test some numbers
print(sqrt(4))       # Output: 2.0
print(sqrt(9))       # Output: 3.0
print(sqrt(-1))      # Output: None
