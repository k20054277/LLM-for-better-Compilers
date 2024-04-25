import json

# Example JSON data
data = '{"name": "John", "age": 30, "city": "New York"}'

# Parse the JSON data
parsed_data = json.loads(data)

print("Name:", parsed_data["name"])
print("Age:", parsed_data["age"])
print("City:", parsed_data["city"])