
# Define a dictionary with keys having strings representing false values
false_values = {
    "zero": "0",
    "empty_list": "[],",
    "empty_tuple": "(),"
}

def check_false(value):
    """
    Check if the given value is false.

    :param value: A value to be checked for falseness.
    :return: True if the value is false, False otherwise.
    """
    return value == False or eval(value)

# Check false values using check_false function
for key, value in false_values.items():
    print(f"Is '{key}' false? - {check_false(value)}")
