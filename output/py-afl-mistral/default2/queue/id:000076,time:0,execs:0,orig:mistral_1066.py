
# Function definition with keyword arguments
def print_info(first_name, last_name, age):
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")
    print(f"Age: {age}")

# Unpacking a dictionary with 'as' keyword
data = {"first": "John", "last": "Doe", "age": 30}
args = data.items()  # This returns a list of tuples [('first', 'John'), ('last', 'Doe'), ('age', '30')]
key_value_pairs = args[0:2]  # Get first two items from the list

print_info(*key_value_pairs, **{k: v for k, v in args[-1:]})
