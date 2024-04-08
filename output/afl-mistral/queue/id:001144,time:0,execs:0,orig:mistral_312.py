
# Function that returns None if a given number is even, and the number itself if it's odd
def is_odd(n):
    if n % 2 == 0:
        return None
    else:
        return n

# Testing the function
print(is_odd(3))   # Output: 3
print(is_odd(4))   # Output: None
