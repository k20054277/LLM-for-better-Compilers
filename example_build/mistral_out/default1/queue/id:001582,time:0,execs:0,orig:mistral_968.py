
def is_even_and_positive(n):
"""
Check if a number is both even and positive
"""
# Using Python's built-in `isinstance()` function, we check if the number is an integer type
if isinstance(n, int) and n > 0:
# Checking if the number is even by using the modulus operator (%). If the remainder of a number divided by 2 is 0, then it's even.
 if n % 2 == 0:
 return True
else:
 return False
# If the input number does not pass the first two conditions (integer and positive), we don't even bother checking for evenness.
