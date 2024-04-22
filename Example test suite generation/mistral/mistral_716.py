
# Define a function to check if a number is even or odd
def is_even(number):
    # If the number is divisible by 2 with no remainder, it's an even number
    return number % 2 == 0

# Test some numbers and print the results
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if is_even(number):
        result = "even"
    else:
        result = "odd"
        
    print(f"{number} is {result}")
