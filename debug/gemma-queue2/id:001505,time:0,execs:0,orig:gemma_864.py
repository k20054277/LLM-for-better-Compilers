
def my_function(x):
    return x * 2

# Demonstration of and and callable
if __name__ == "__main__":
    a = 5
    b = 10

    # Using and operator to check if a and b are both greater than 5
    if a > 5 and b > 5:
        print("Both a and b are greater than 5")

    # Calling the my_function function with a parameter of 5
    result = my_function(5)

    # Printing the result
    print("The result of the function call is:", result)
