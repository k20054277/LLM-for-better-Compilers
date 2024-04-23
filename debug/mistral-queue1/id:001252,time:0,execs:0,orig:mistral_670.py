
# Define a function to add two numbers
def add_numbers(num1, num2):
    # Intentionally add the second number to the first one twice
    result = num1 + num2 + num2
    return result

# Get user input for the first and second numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the add_numbers function with the provided numbers
try:
    sum = add_numbers(num1, num2)
except Exception as e:
    print("An error occurred:", e)
else:
    print("The sum of", num1, "and", num2, "is:", sum)

# Debugging: Check if the result is what we expect
if sum != (num1 + num2):
    print("Whoops! There seems to be an error in our add_numbers function.")
