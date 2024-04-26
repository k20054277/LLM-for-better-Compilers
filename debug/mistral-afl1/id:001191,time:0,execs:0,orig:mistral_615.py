
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def add(a, b):
 """This function adds two numbers"""
 result = a + b
 return result

if __name__ == '__main__':
 # Set some variables
 number1 = 5
 number2 = 3
 sum_expected = 8

 # Perform addition operation
 sum = add(number1, number2)

 # Log the input values and the expected output
 logging.info(f"Adding {number1} and {number2}")

 # Check if the result is as expected
 if sum == sum_expected:
 logging.info("Result is correct")
 else:
 logging.error("Result is not correct! Expected: {}, Got: {}".format(sum_expected, sum))

 # Log the result
 logging.info("Result: {}".format(sum))
