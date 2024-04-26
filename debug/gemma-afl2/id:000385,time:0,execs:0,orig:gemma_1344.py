
# This Python program demonstrates the use of assert and while.

# Define a function to check if a number is even.
def is_even(n):
    return n % 2 == 0

# Assert that the function returns True for even numbers.
assert is_even(4) is True
assert is_even(6) is True

# Assert that the function returns False for odd numbers.
assert is_even(5) is False
assert is_even(7) is False

# While loop to iterate over even numbers from 1 to 10.
while is_even(n):
    print(n)
    n += 2

# Print the final message.
print("Finished!")
