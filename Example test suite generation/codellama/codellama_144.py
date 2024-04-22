import json

# Create a dictionary with some data
data = {'name': 'John Doe', 'age': 30, 'city': 'New York'}

# Convert the dictionary to JSON format
json_data = json.dumps(data)

# Print the JSON formatted data
print(json_data)

# Parse the JSON formatted data back to a Python dictionary
parsed_data = json.loads(json_data)

# Print the parsed data
print(parsed_data)