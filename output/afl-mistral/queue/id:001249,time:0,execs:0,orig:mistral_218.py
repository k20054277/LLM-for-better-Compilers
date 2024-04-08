
# Function to check if a number is even or odd
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Testing the function with some numbers
numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if is_even(num):
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")
