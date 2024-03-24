
import json

# Sample JSON data
data = '''
{
  "users": [
    { "name": "John", "age": 30, "is_active": true },
    { "name": "Jane", "age": 25, "is_active": false },
    { "name": "Doe", "age": 45, "is_active": true }
  ]
}
'''

# Parse JSON data
parsed_data = json.loads(data)

# Filter users based on condition
filtered_users = [user for user in parsed_data["users"] if user["age"] > 30 and user["is_active"] is True]

print("Users who are older than 30 and active:")
for user in filtered_users:
    print(f"Name: {user['name']}, Age: {user['age']}")
