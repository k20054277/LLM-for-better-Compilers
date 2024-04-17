
# Using assert statement
def add(x, y):
    assert type(x) is (int or float), "x should be either integer or float"
    assert type(y) is (int or float), "y should be either integer or float"
    return x + y

try:
    result = add("3", 5)
except AssertionError as e:
    print(e)
else:
    print("Addition Result:", result)

# Using right shift bitwise operator (>>)
def right_shift(number, shifts):
    assert type(number) is int, "number should be an integer"
    assert type(shifts) is int, "shifts should be an integer"
    return number >> shifts

try:
    result = right_shift("5", 2)
except AssertionError as e:
    print(e)
else:
    binary_result = bin(result)[2:].zfill(8)
    print("Right Shift Result (binary):", binary_result)
