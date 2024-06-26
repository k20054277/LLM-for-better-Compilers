def reverse_string(my_str):
    assert isinstance(my_str, str), "Input must be a string"
    return "".join(reversed(my_str))

# Test the function with different inputs
assert reverse_string("hello") == "olleh"
assert reverse_string("abcdef") == "fedcba"
assert reverse_string("") == ""