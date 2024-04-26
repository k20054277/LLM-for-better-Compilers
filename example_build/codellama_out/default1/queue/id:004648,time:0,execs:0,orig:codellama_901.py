import json

# Define a dictionary with some data
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# Convert the dictionary to JSON format
json_data = json.dumps(data)

print(json_data)

# Load the JSON data back into a Python dictionary
loaded_data = json.loads(json_data)

print(loaded_data)