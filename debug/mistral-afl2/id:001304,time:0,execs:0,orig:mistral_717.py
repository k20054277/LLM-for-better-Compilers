
# Define a function to calculate base raised to the power of exponent
def power(base, exponent):
    result = base ** exponent
    return result

# Base and exponent values for demonstration
base = 2
exponent = 3

# Calculate the base raised to the power of the exponent using the power function
raised_to_power = power(base, exponent)

# Print the result
print("{} raised to the power of {} is:".format(base, exponent), raised_to_power)

# Use True in a simple conditional statement
if True:
    print("This statement will always be true and therefore execute.")

# Define a number and check if it's positive
number = 5

if number > 0:
    print("{} is a positive number".format(number))
else:
    print("{} is a non-positive number".format(number))
