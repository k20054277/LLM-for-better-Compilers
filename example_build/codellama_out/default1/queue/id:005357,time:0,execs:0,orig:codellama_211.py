# This program demonstrates the use of False and hasattr in Python

def demo(x):
  if hasattr(x, 'is_false'):
    print("The object has the attribute 'is_false'")
  else:
    print("The object does not have the attribute 'is_false'")

# Test with a boolean value
demo(False)

# Test with an integer value
demo(123)

# Test with a string value
demo('hello')