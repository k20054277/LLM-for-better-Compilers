
# A simple list of tuples, where the second element can be `None`
data = [(1, None), (2, 3), (None, 4), (5,)]

# A simple function that returns its argument if it's not None, otherwise returns 0
def process_value(val):
    return val if val is not None else 0

# Using map to apply 'process_value' on every value in data list
result = list(map(process_value, data))

print("Original Data:")
print(data)
print("\nProcessed Data:")
print(result)
