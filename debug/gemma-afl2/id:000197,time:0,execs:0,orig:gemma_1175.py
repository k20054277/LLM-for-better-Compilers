
import json

# Create a dictionary
my_dict = {"name": "John Doe", "age": 30, "interests": ["music", "reading", "coding"]}

# Convert the dictionary to JSON
my_json_str = json.dumps(my_dict)

# Print the JSON string
print(my_json_str)

# Convert the JSON string back to a dictionary
my_new_dict = json.loads(my_json_str)

# Print the new dictionary
print(my_new_dict)
