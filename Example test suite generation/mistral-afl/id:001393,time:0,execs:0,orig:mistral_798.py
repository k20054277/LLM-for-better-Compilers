
# Example using 'and'
def is_even(n):
    """Check if number is even."""
    return n % 2 == 0

def greater_than_ten(n):
    """Check if number is greater than ten."""
    return n > 10

number = int(input("Enter a number: "))

if is_even(number) and greater_than_ten(number):
    print("The number is even and greater than ten.")
else:
    print("The number is either not even or not greater than ten.")
