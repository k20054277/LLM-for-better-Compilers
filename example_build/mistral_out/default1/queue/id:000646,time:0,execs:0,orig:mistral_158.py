
# Function with a false condition
def is_even(number):
    if number % 2 != 0:
        return False
    else:
        return True

# Function with return value
def add_numbers(x, y):
    sum = x + y
    return sum

if __name__ == "__main__":
    # Check if a number is even using the is_even function
    number = 5
    is_it_even = is_even(number)
    print(f"{number} is even: {is_it_even}")

    # Add two numbers using the add_numbers function
    x = 3
    y = 7
    sum = add_numbers(x, y)
    print(f"The sum of {x} and {y} is: {sum}")
