
def calculate_mean(numbers):
    """Calculate the mean of given numbers"""
    total = sum(numbers)
    mean = total / len(numbers)
    return mean

# List of numbers to calculate mean
numbers = [1, 2, 3, 4, 5]
mean = calculate_mean(numbers)

print("Mean: ", mean)

# Assert statement for checking if the calculated mean is equal to the expected mean (5 in this case)
assert mean == 5, "Calculated mean doesn't match with the expected mean."

# Unpacking a list to pass elements as individual arguments to a function
def print_numbers(a, b, c):
    """Prints three given numbers"""
    print(f"Number 1: {a}")
    print(f"Number 2: {b}")
    print(f"Number 3: {c}")

numbers = [1, 2, 3]
print_numbers(*numbers)
