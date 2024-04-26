
# This Python program demonstrates the use of and and repr

# Define a function to demonstrate the use of and and repr
def demonstrate_and_repr():
    # Create a list of integers
    numbers = [1, 2, 3, 4, 5]

    # Use the and operator to check if all elements in the list are greater than 2
    if all(number > 2 for number in numbers):
        print("All elements in the list are greater than 2")

    # Use the repr function to print the representation of the list
    print(repr(numbers))

# Call the demonstrate_and_repr function
demonstrate_and_repr()
