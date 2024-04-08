
# Assigning None to a variable
none_value = None
print("Value of none_value is:", none_value)

# Using if condition with None
def get_data():
    data = None
    if data is not None:
        print("Data is available")
        return data
    else:
        print("No data available")
        return None

print("Getting data from the function:")
my_data = get_data()
if my_data is not None:
    print("My data is:", my_data)
else:
    print("No data received")

# Using list with None as an element
numbers = [1, 2, None, 4, 5]
print("List of numbers:", numbers)

# Using tuples with None as an element
tuple_values = (1, "Two", None)
print("Tuple values:", tuple_values)
