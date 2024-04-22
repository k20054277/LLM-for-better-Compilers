
import json

# Create a Python dictionary
data = {
    "name": "John Doe",
    "is_student": True,
    "age": 25
}

print("Original Python Dictionary:")
print(data)

# Convert Python dictionary to JSON format
json_data = json.dumps(data)

print("\nJSON representation:")
print(json_data)

# Check if 'is_student' value is True
if data["is_student"]:
    print("\n'is_student' value is True.")
else:
    print("\n'is_student' value is False.")
