
def is_even(n):
    """Check if number is even"""
    return n % 2 == 0

for i in range(1, 11):
    if not is_even(i):
        print("Skipping odd number:", i)
        continue
    print("Even number:", i)
