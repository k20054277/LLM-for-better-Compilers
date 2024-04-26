
# Function to check if a number is even or odd
def is_even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Get user input and convert it to integer
user_input = input("Enter an integer: ")
try:
    num = int(user_input)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
else:
    # Check if the number is even or odd using assert statement
    result = is_even_or_odd(num)
    assert type(result) == str, "is_even_or_odd function should return a string"
    print(f"The number {num} is {result}")
