
# This is a simple Python program that uses 'and' operator and 'continue' statement

# Function to check if a number is even or prime
def check_even_or_prime(num):
    # Check if number is even using 'and' operator
    if num % 2 == 0 and num > 1:
        print(f"{num} is an even number.")
        return
    
    # Start checking for prime number from 2 up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            continue
    
    # If number passes all the checks, then it is an odd prime number
    if num > 1:
        print(f"{num} is an odd prime number.")

# Testing the function with some numbers
check_even_or_prime(5)  # Output: 5 is an odd prime number.
check_even_or_prime(6)  # Output: 6 is an even number.
check_even_or_prime(13) # Output: 13 is an odd prime number.
