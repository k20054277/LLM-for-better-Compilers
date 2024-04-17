
# Define a function that takes two arguments, one is expected to be a dictionary, the other can be None
def process_data(data=None, key='default'):
    if data is None:
        print("No data provided. Using default instead.")
        data = {}

    # Check if key exists in the data dictionary
    if key not in data:
        print(f"Key '{key}' does not exist in the dictionary.")
        return

    value = data[key]
    print(f"Value of key '{key}' is: {value}")

# Use the function with a dictionary
my_data = {'name': 'John', 'age': 30}
process_data(my_data, 'name')

# Use the function without a dictionary
process_data(None, 'age')
