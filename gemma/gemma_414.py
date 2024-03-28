
# False and Algorithm

# Define a function to find the maximum of two numbers
def find_maximum(num1, num2):
    # If num1 is greater than num2, return num1
    if num1 > num2:
        return num1
    # Otherwise, return num2
    else:
        return num2

# Create two numbers
num1 = 10
num2 = 20

# Find the maximum of num1 and num2
maximum = find_maximum(num1, num2)

# Print the maximum
print("The maximum of num1 and num2 is:", maximum)

# Output:
# The maximum of num1 and num2 is: 20
