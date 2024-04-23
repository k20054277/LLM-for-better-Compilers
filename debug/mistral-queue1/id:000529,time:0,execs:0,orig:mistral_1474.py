
# Example using assert statement
def add(x, y):
    result = x + y
    assert result > 0, "Error: The sum is not positive"
    return result

try:
    print(add(-2, 3))
except AssertionError as e:
    print("Exception occurred:", e)
