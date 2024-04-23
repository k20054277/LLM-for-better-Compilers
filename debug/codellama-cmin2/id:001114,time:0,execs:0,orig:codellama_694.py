import json

# Define a dictionary with some key-value pairs
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'NYC'
}

# Convert the dictionary to a JSON string
json_string = json.dumps(data)

print(json_string)