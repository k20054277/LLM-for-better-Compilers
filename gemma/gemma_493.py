
def function_with_none(x):
    if x is None:
        return None
    else:
        return x * 2


# Demonstrating the use of None and returnvalue
a = None
print(function_with_none(a))  # Output: None

b = 10
print(function_with_none(b))  # Output: 20
