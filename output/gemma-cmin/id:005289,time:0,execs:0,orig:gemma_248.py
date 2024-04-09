
import json

# Create a dictionary
data = {"name": "John Doe", "age": 30, "interests": ["reading", "music", "hiking"]}

# Convert the dictionary to JSON
json_data = json.dumps(data)

# Print the JSON data
print(json_data)

# Decode the JSON data
decoded_data = json.loads(json_data)

# Print the decoded data
print(decoded_data)
