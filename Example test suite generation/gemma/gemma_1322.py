
def divisible_by_three(n):
    """Checks if a number is divisible by three.

    Args:
        n: The number to check.

    Returns:
        True if n is divisible by three, False otherwise.
    """

    if n % 3 == 0:
        return True
    else:
        continue

# Test code
for num in range(1, 11):
    if divisible_by_three(num):
        print(num + " is divisible by three.")
