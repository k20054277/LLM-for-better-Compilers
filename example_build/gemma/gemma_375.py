
import sys

# False boolean value
is_active = False

# Print True or False based on the boolean value
print(is_active)

# Check if the program is running in debug mode
if sys.gettrace() is not None:
    print("Program is in debug mode")

# Print the number of arguments passed to the program
print(len(sys.argv))
