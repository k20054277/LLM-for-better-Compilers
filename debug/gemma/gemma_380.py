
import json

# Define a dictionary
data = {"name": "John Doe", "age": 30, "interests": ["music", "reading", "coding"]}

# Print the dictionary
print(data)

# Convert the dictionary to JSON
json_data = json.dumps(data)

# Print the JSON data
print(json_data)

# Parse the JSON data
parsed_data = json.loads(json_data)

# Print the parsed data
print(parsed_data)

# Check if the data is False
if data is False:
    print("Data is False")

# Check if the data is True
if data is True:
    print("Data is True")
