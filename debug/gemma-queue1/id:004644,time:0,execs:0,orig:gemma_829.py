
# This Python program demonstrates the use of and and break statements

# Define a function called my_function
def my_function():
    # Iterate over a range of numbers from 1 to 10
    for num in range(1, 11):
        # Check if the number is divisible by both 2 and 3
        if num % 2 == 0 and num % 3 == 0:
            # Break out of the loop
            break
        # Print the number
        print(num)

# Call the my_function function
my_function()

# Output:
# 6
