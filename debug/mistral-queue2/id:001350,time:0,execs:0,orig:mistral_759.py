
# Define two variables with initial values
x = 5
y = 10

# Check if 'x' is less than 'y' using a Boolean expression
is_x_less_than_y = x < y

# Print the result of the comparison (Boolean value)
print(f"Is {x} less than {y}? -> {is_x_less_than_y}")

# Assign new values to 'x' and 'y' based on a condition
if is_x_less_than_y:
    x, y = y, x

# Print the updated values of 'x' and 'y'
print(f"Now x = {x} and y = {y}")
