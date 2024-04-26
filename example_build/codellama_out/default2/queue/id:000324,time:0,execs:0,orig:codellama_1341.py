def convert_to_string(number):
    assert type(number) == int, "The number must be an integer"
    return str(number)

print(convert_to_string(123)) # Output: "123"
print(convert_to_string("hello")) # Output: "TypeError: The number must be an integer"