
# Recursive function to find factorial of a given number
def recursive_function(n):
    # Base case: if n is 0, return 1 (factorial of 0 is 1)
    if n == 0:
        return True  # In this specific case, we could also return 1, but for the sake of the example, we'll use 'True' instead.
    
    # Recursive call: multiply 'n' with the result of recursively calling the function with 'n-1' as an argument
    else:
        return recursive_function(n - 1) * n

# Testing the recursive function with some inputs
number = 5
result = recursive_function(number)
print(f"The factorial of {number} is {result}")
