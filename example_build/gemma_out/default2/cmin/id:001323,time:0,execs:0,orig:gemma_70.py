
# This Python program demonstrates the use of and and continue

# Define a function called my_function
def my_function(num):
    # If the number is even and divisible by 3, continue
    if num % 2 == 0 and num % 3 == 0:
        continue

    # Print the number
    print(num)

# Iterate over a range of numbers from 1 to 10
for num in range(1, 11):
    # Call the my_function function
    my_function(num)
