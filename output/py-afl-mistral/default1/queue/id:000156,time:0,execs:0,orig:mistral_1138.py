
import json

# Data in dictionary format
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Convert dictionary to JSON string using json.dumps()
json_str = json.dumps(data)
print("JSON String: ", json_str)

# Parse JSON string back to dictionary using json.loads()
parsed_data = json.loads(json_str)

# Using 'as' keyword to assign the parsed data directly to a variable
data_from_json as new_data

print("Original Data: ", data)
print("Data from JSON: ", new_data)

# Check if both data and new_data are same
if id(data) == id(new_data):
    print("Both are the same object")
else:
    print("Both are different objects")
