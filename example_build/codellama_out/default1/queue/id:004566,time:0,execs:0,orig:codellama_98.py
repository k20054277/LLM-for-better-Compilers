def print_and(a, b):
    return a and b

def get_attribute(obj, attr):
    return getattr(obj, attr)

print(print_and(True, True))  # Output: True
print(print_and(True, False))  # Output: False
print(get_attribute('hello', 'len'))  # Output: