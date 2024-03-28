
# This Python program demonstrates the use of True and next

# Define a function that returns True if the input number is even, next otherwise
def is_even(num):
    return num % 2 == 0

# Iterate over a range of numbers and print those that are even
for num in range(10):
    if is_even(num):
        print(num)

# Print the next number after the current number
print(next(num) for num in range(10) if is_even(num) else None)
