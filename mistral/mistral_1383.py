
import json

# Define a dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Convert the dictionary to JSON format
json_data = json.dumps(data)

# Print the JSON data for verification
print("JSON Data:")
print(json_data)

# Parse the JSON string back to a dictionary
parsed_data = json.loads(json_data)

# Use assert statements to check equality
assert data == parsed_data, "Error! Original data and parsed data are not equal."
print("Original Data:")
print(data)
print("Parsed Data:")
print(parsed_data)
