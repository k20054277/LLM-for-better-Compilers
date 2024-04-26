
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def square_root(number):
 """
 Calculate the square root of a given number.
 If the number is negative, return False.
 """
 try:
 result = number ** 0.5
 except Exception as e:
 logging.exception("An error occurred while calculating the square root: %s", str(e))
 else:
 logging.info(f"The square root of {number} is {result}")
 return result if number >= 0 else False

# Test cases
print(square_root(9)) # 3.0
print(square_root(-1)) # False
print(square_root(25)) # 5.0
