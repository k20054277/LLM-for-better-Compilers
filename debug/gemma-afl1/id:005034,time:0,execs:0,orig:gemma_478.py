
# Define a function to find the maximum of two numbers

def find_maximum(num1, num2):
    # If num1 is None, return num2
    if num1 is None:
        return num2

    # If num2 is None, return num1
    if num2 is None:
        return num1

    # Otherwise, return the maximum of num1 and num2
    return max(num1, num2)

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Find the maximum of the two numbers
maximum = find_maximum(num1, num2)

# Print the maximum number
print("The maximum number is:", maximum)
