
# Define two variables with some values
num1 = 10
num2 = 3

# Perform division operation and assign result to a new variable
result = num1 / num2

print("Result of the division: ", result)

# Assign the quotient to num1 using /= operator and check if the condition is false
num1 /= num2
print("Value of num1 after using /= operator: ", num1)
print("Is the condition (num1 == num2) false? ", num1 != num2)

# Now, let's use False value to control a conditional statement
if not(False):
    print("This block is executed only if False is replaced with True")
else:
    print("This block is executed because False is True in this context (it isn't!)")
