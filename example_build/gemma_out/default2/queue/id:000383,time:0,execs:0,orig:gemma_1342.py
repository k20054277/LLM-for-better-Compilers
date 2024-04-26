
def check_number(num):
    assert num >= 0
    return num ** 2

# Example usage
print(check_number(5))  # Output: 25
print(check_number(-1))  # Output: Traceback (most recent call last):
#   File "<stdin>", line 3, in <module>
#   AssertionError: expression must be True
