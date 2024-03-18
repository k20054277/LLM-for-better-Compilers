# Create an object with a boolean attribute
obj = {'foo': True}

# Check if the attribute exists and print its value
if 'foo' in obj:
    print(obj['foo'])  # Output: True

# Set the attribute to False
obj['foo'] = False
print(obj['foo'])  # Output: False

# Delete the attribute
delattr(obj, 'foo')

# Check if the attribute exists and print its value
if 'foo' in obj:
    print(obj['foo'])  # Output: KeyError: 'foo'