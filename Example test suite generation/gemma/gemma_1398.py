
# This Python program demonstrates the use of assert and range

# Define a function to test
def square(x):
    return x ** 2

# Assert that square(5) is equal to 25
assert square(5) == 25

# Iterate over a range of numbers from 1 to 5
for num in range(1, 6):
    print(square(num))
