import json

# Creating a dictionary with a key-value pair where the value is None
my_dict = {'name': 'John', 'age': 30, 'car': None}

print(json.dumps(my_dict)) # Output: {"name": "John", "age": 30, "car": null}

# Loading a JSON file with a value of None
with open('data.json', 'r') as f:
    data = json.load(f)
print(data['age']) # Output: 25
print(data['car']) # Output: None