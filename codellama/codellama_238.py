import json

# create a dictionary with a false value
my_dict = {"key1": "value1", "key2": False}

# convert the dictionary to JSON format
json_string = json.dumps(my_dict)

# print the JSON string
print(json_string)