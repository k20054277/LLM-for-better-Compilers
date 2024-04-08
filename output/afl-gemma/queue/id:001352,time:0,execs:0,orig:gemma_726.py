
# This Python program demonstrates the use of True and algorithms

# Define a function to find the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Print the factorial of 5
print(factorial(5))

# Check if a number is even
def is_even(n):
    return n % 2 == 0

# Print whether 6 is even
print(is_even(6))

# Use True and False to check if a condition is true or false
if True and False:
    print("True and False are true")

# Use an algorithm to find the largest number in an array
def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num

    return largest

# Print the largest number in an array
print(find_largest([10, 20, 30, 40, 50]))
