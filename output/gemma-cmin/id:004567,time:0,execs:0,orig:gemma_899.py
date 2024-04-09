
# This Python program demonstrates the use of and and next

# Define a function called my_function
def my_function(n):
    # Use the and operator to check if n is greater than 5 and less than 10
    if n > 5 and n < 10:
        # Print the value of n
        print(n)

    # Use the next function to get the next integer greater than n
    n_next = next(i for i in range(n+1, 11) if i > n)

    # Print the value of n_next
    print(n_next)

# Call the my_function function with different values
my_function(3)
my_function(7)
my_function(12)
