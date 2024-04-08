# Testing the use of True and finally in Python

print("Testing the use of True and finally")

try:
    # This code will raise an error
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
    # The code in the except block is executed when an exception is raised
finally:
    print("This code is always executed, regardless of whether an error was raised or not")