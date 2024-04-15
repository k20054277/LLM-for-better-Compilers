
# Function that returns None if the given number is even, else returns the number squared
def is_even(num):
    """
    This function checks if a given number is even or not.
    If the number is even, it returns None. Else it returns the number squared.
    """
    if num % 2 == 0:
        return None
    else:
        return num ** 2

# Testing the function
num = int(input("Enter a number: "))
result = is_even(num)

if result is not None:
    print(f"Square of given number is {result}")
else:
    print("Given number is even")
