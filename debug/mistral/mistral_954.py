
# First, we define two boolean functions that return True or False based on certain conditions
def is_odd(n):
    return n % 2 != 0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Now we use the and operator to ensure both conditions are met before executing a print statement
if is_odd(num) and is_prime(num):
    print("The number", num, "is odd and prime")
else:
    print("The number", num, "does not meet both conditions")
