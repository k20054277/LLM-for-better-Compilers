
# Example 1: Comparison with False using 'and' operator
number = -5
if number > 0 or not (number < 0):  # Use of 'not' negates the condition, equivalent to 'False'
    print("Number is non-negative")
else:
    print("Number is negative")

# Output: Number is negative

# Example 2: Comparison with False using 'if' statement
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

if not is_even(3):  # Compare with False by negating the result of the function
    print("Number is odd")
else:
    print("Number is even")

# Output: Number is odd
