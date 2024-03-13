
# Define some functions
def function1(x):
    return x > 0

def function2(x):
    return x % 2 == 0

def composite_function(x):
    return x > 0 and x % 2 == 0

# Check if a function is callable
print("Is function1 callable? ", callable(function1)) # True
print("Is composite_function callable? ", callable(composite_function)) # True

# Use and operator to combine the conditions
def check_even_positive(x):
    return x > 0 and x % 2 == 0

if check_even_positive(10):
    print("10 is even and positive")

if check_even_positive(-5):
    print("-5 is even and positive")
