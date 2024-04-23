
# Function to check if given number is even or odd
def is_even(num):
    return num % 2 == 0

# Function to find all even numbers in a list using list comprehension
def find_evens(numbers):
    evens = [num for num in numbers if is_even(num)]
    return evens

# Test the function with a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = find_evens(numbers)

print("Even numbers in given list:")
print(evens)
