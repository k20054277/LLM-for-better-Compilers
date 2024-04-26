
# False and iter

# Define a function to demonstrate False and iter
def demonstrate_false_and_iter():
    # Create a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Iterate over the list using False as a condition
    for number in numbers if False:
        print(number)

    # Iterate over the list using iter()
    for number in iter(numbers):
        print(number)

# Call the function
demonstrate_false_and_iter()
