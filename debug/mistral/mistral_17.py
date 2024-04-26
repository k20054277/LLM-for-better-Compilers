
def divisor(num):
    """
    This function checks if given number has a divisor other than 1 and itself.
    """
    for i in range(2, num):
        if num % i == 0:
            return True
    return False

try:
    num = int(input("Enter a number: "))

    while divisor(num):
        print(f"The number {num} has divisors other than 1 and itself.")
        num = int(input(f"Enter another number ({num}) without divisors other than 1 and itself: "))

except ValueError as ve:
    print("Invalid input. Please enter an integer.")

finally:
    print("\nThe program has finished executing.")
