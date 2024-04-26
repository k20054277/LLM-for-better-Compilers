
# Initialize some variables
x = 0
y = 5

# Use and keyword and assign a new value to x if y is greater than 3
if y > 3:
    x = x and 1

print("Value of x after if statement execution: ", x)  # Output: 0

# Use and keyword with some other condition and compound assignment operator
x = 5
y = 10
z = 2
if y > 3 and z < 5:
    x += 1

print("Value of x after if-else statement execution: ", x)  # Output: 5
