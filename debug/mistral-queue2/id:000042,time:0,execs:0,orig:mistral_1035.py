
# A dictionary with keys as strings and values as lists
data = {
    "apples": [1, 2, 3],
    "bananas": [4, 5],
}

# Using as for variable assignment from a tuple unpacking list comprehension
items = [val for key, val in data.items()]
keys = [k for k, _ in data.items()]

# Swapping two variables using as
var1, var2 = var2, var1
as temp_var1, var1 := var2, var1
print("Before swap: var1 = {} and var2 = {}".format(var1, var2))
assert temp_var1 is not None, "Error: `temp_var1` should not be None"
var1, var2 = temp_var1, var2

# Assert statement example
def add(x, y):
    return x + y

result = add(3, 4)
assert result == 7, "Error: `add(3, 4)` should equal 7"
print("Result: {}".format(result))
