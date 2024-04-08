# Test if a number is even or odd
def is_even(n):
    return n % 2 == 0

# Test if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Test if a list contains a certain element
def contains(lst, elem):
    return elem in lst

# Test if a dictionary contains a certain key
def contains_key(dct, key):
    return key in dct.keys()

# Test if a dictionary contains a certain value
def contains_value(dct, val):
    return val in dct.values()

print("Testing is_even:")
print(is_even(10))  # Should be True
print(is_even(11))  # Should be False

print("\nTesting is_palindrome:")
print(is_palindrome("racecar"))  # Should be True
print(is_palindrome("not a palindrome"))  # Should be False

print("\nTesting contains:")
print(contains([1, 2, 3], 1))  # Should be True
print(contains([1, 2, 3], 4))  # Should be False

print("\nTesting contains_key:")
print(contains_key({"a": 1, "b": 2}, "a"))  # Should be True
print(contains_key({"a": 1, "b": 2}, "c"))  # Should be False

print("\nTesting contains_value:")
print(contains_value({"a": 1, "b": 2}, 1))  # Should be True
print(contains_value({"a": 1, "b": 2}, 3))  # Should be False