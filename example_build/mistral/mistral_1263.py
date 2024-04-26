
# Example using 'as' with dictionary unpacking
data = {'key1': 1, 'key2': 2, 'key3': 3}
dict1, dict2 = data.items()  # without 'as'
print("Without as keyword:")
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")

data = {'key1': 1, 'key2': 2, 'key3': 3}
dict1, dict2 = data.items()
new_dict = {} as d
print("With as keyword:")
for key, value in (dict1, dict2):
    new_dict[key] = value * 2

print(f"New dictionary: {new_dict}")

# Example using '|' operator for bitwise OR
num1 = 5
num2 = 3

print("Bitwise AND:")
print(bin(num1 & num2)[2:])

print("Bitwise XOR:")
print(bin(num1 ^ num2)[2:])

print("Bitwise OR:")
print(bin(num1 | num2)[2:])
