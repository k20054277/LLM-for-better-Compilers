
def check_numbers(numbers):
    for number in numbers:
        # Assertion to check if number is non-negative
        assert number >= 0, f"Error: Number {number} is negative."
        # Check if number is even and print it if it is
        if number % 2 == 0:
            print(number)
        else:
            continue

# Test the function with a list of numbers
numbers = [3, 5, 10, -2, 7]
check_numbers(numbers)
