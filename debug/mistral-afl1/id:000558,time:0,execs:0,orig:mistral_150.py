
# Recursive function to check if a number is negative
def is_negative(number):
    # Base case: if number is less than zero, return True
    if number < 0:
        return True
    else:
        # Recursive call: check if the absolute value of the number is negative
        return is_negative(-abs(number))

# Test cases
print(is_negative(-5))           # Should print: True
print(is_negative(-1))           # Should print: True
print(is_negative(-0.25))        # Should print: True
print(is_negative(0))            # Should print: False
print(is_negative(3))            # Should print: False
print(is_negative(100))          # Should print: False
