
# Define a function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Assert that the factorial function works correctly
assert factorial(5) == 120

# Iterate over a range of numbers and calculate their factorials
for i in range(1, 6):
    print(factorial(i))
