
# Function to check if a number is even or odd
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Testing the function
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    result = is_even(num)
    print("{} is {}".format(num, "even" if result else "odd"))
