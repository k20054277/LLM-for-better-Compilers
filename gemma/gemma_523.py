
# Define a function that takes a parameter 'a' and returns 'None' if 'a' is None or 'a' is less than 5
def check_a(a):
    if a is None or a < 5:
        return None
    else:
        return a

# Demonstrate the use of the function
a = None
print(check_a(a))  # Output: None

a = 4
print(check_a(a))  # Output: 4

a = 2
print(check_a(a))  # Output: None
