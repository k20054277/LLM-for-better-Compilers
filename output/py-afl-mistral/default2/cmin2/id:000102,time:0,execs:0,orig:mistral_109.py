
import json

# Define an empty dictionary
data = {}

# Set a key with a False value
data['key_with_false'] = False

# Check if 'key_with_false' is present and its value is False
if 'key_with_false' in data and data['key_with_false'] is False:
    print("The value of 'key_with_false' is False")
else:
    print("The value of 'key_with_false' is not False or not present in the dictionary")

# Convert the dictionary to a JSON string
json_string = json.dumps(data)

# Print the JSON string
print("\nJSON representation of the dictionary:")
print(json_string)

# Try parsing the JSON string back into a dictionary
try:
    parsed_data = json.loads(json_string)
except json.JSONDecodeError as e:
    print(f"\nFailed to parse JSON: {e}")
else:
    # Check if 'key_with_false' still has the same value
    if 'key_with_false' in parsed_data and parsed_data['key_with_false'] is False:
        print("The value of 'key_with_false' in the parsed dictionary is also False")
    else:
        print("The value of 'key_with_false' in the parsed dictionary is different from the original one")
