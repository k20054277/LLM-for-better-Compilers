
# This is a simple program that checks if a number is even or odd using a boolean variable

def is_even(number):
    # Initialize the flag with False value
    is_even = False
    
    # Check if number is even
    if number % 2 == 0:
        is_even = True
        
    return is_even

# Check some numbers and print the result
print("Is 10 an even number? ", is_even(10))
print("Is 5 an even number? ", is_even(5))
print("Is 3 an odd number? ", not is_even(3))

# Using help() function to get information about a built-in function or module
print("\nUsing help():")
help(abs) # Prints the documentation for the abs() function
