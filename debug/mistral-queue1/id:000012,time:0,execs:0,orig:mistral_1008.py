
# Define two variables with integer values
num1 = 5
num2 = 7

# Use the 'and' operator to check if two conditions are true
# In this case, both conditions must be true for the whole expression to be true
if num1 <= 10 and num2 <= 10:
    print("Both numbers are less than or equal to 10")

# Use the 'and' operator with other boolean expressions as well
# For example, checking if a number is even and positive
if num % 2 == 0 and num > 0:
    print("The number is even and positive")
else:
    print("The number is odd or negative")
