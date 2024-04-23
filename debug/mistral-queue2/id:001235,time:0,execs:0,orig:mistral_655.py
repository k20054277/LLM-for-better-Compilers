
def is_positive(num):
    """
    This function checks if given number is positive, returns True if it is, otherwise False
    """
    if num > 0:
        return True
    else:
        return False

# Testing the function
num = int(input("Enter a number: "))
result = is_positive(num)
print(f"The number {num} is {'positive' if result else 'non-positive'}.")
