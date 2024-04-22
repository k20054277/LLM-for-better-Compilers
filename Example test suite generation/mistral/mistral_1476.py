
def add_numbers(x, y):
    result = x + y
    assert type(result) is int, "Addition must return an integer."
    return result

a = 10
b = 5
c = 3.14
result_a = add_numbers(a, b)
result_c = add_numbers(a, c)
print("Result of adding two integers: ", result_a)
print("Result of adding an integer and a float: ", result_c)
