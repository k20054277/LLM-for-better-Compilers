
def is_prime(n):
    """Return True if n is a prime number."""
    if n <= 1:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return n in (2, 3)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
