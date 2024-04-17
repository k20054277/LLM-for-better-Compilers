# Define two variables, x and y, and assign them some values
x = 5
y = 10

# Use the "and" operator to check if both variables are greater than 0
if x > 0 and y > 0:
    print("Both x and y are greater than 0")
else:
    print("At least one of x or y is not greater than 0")

# Use the "[]" syntax to create a list with values from x to y
my_list = [x for i in range(y)]
print(my_list)