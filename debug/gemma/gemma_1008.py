
# Define a function to demonstrate AND and dependency
def demonstrate_and_dependency(a, b):
    # Check if both a and b are greater than 5
    if a > 5 and b > 5:
        print("Both a and b are greater than 5")
    else:
        print("One or both of a and b are not greater than 5")

# Demonstrate the function with different values
demonstrate_and_dependency(6, 7)  # Output: Both a and b are greater than 5
demonstrate_and_dependency(4, 8)  # Output: Both a and b are greater than 5
demonstrate_and_dependency(3, 6)  # Output: One or both of a and b are not greater than 5
