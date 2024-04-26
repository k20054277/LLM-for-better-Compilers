
# Define some global variables
x = 0
y = 0

def my_function():
    global x, y  # Declare x and y as global variables in this function
    x = 10
    y = 20

if x < 5 and y > 10:  # Logical AND operation between two conditions
    print("Condition is met")
else:
    print("Condition is not met")

my_function()  # Change the values of global variables x and y

if x < 5 and y > 10:  # Check conditions after changing the global variables
    print("New condition is met")
else:
    print("New condition is not met")

print("Global variables' values: x =", x, "and y =", y)
