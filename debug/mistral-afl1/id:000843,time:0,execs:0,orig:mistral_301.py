
# Define a function that takes two arguments and returns their quotient and remainder
def my_custom_division(a, b):
    q, r = divmod(a, b)  # Use divmod to get the quotient and remainder
    print(f"Quotient: {q}, Remainder: {r}")
    
# Call the function with some arguments (and one argument as None)
my_custom_division(10, 3)
my_custom_division(10, None)

# Set a variable to None and print it
none_var = None
print("None value: ", none_var)
