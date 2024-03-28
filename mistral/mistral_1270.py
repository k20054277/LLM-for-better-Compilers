
# Function to check if a number is even or odd
def is_even(number):
    return not number % 2

# Get user input for the number
num = int(input("Enter a number: "))

# Apply the logic using 'as' and 'not'
if not (num % 2) as result:
    print(f"The given number {num} is even")
else:
    print(f"The given number {num} is odd")
