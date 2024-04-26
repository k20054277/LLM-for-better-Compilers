
# Define a function to check if an object is a string
def is_string(obj):
  """Checks if an object is a string.

  Args:
    obj: The object to check.

  Returns:
    True if obj is a string, False otherwise.
  """

  return isinstance(obj, str) or isinstance(obj, unicode) or isinstance(obj, str)

# Demonstrate the use of False and isinstance
print(is_string(False))  # Output: False
print(is_string(1))  # Output: False
print(is_string("hello"))  # Output: True
print(is_string(u"hello"))  # Output: True
print(is_string("123"))  # Output: True
