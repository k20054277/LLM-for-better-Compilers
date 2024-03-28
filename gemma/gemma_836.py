
# This Python program demonstrates the use of try, except, and finally keywords.

try:
    # Attempt to execute the following code.
    print(10 / 3)
except ZeroDivisionError:
    # Catch the ZeroDivisionError exception and print an error message.
    print("Error: division by zero is not allowed.")
finally:
    # The finally block will execute regardless of whether an exception occurs or not.
    print("The program has executed the try-except-finally block.")

# Output:
# 3
# The program has executed the try-except-finally block.
