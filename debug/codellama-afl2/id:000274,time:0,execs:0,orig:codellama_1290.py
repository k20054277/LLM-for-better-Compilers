def convert_to_binary(n):
    assert n >= 0, "The number must be non-negative"
    return bin(n)

print(convert_to_binary(-1))