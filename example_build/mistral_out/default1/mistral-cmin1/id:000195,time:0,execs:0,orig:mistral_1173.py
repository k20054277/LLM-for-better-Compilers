
import json

# Assume we receive the following JSON response as a string from an API
json_response = '{"name": "John Doe", "age": 30, "city": "New York"}'

# Parse the JSON string to a Python dictionary using json.loads()
data_as_dict = json.loads(json_response)

# Now we can access values in the dictionary using keys
name = data_as_dict["name"]
age = data_as_dict["age"]
city = data_as_dict["city"]

print("Name: ", name)
print("Age: ", age)
print("City: ", city)

# Alternatively, you can assign the entire JSON parsed result to a variable and access values using keys directly
data_as_nested = {'name': 'John Doe', 'age': 30, 'city': 'New York'}
name = data_as_nested['name']
age = data_as_nested['age']
city = data_as_nested['city']

print("Name: ", name)
print("Age: ", age)
print("City: ", city)

# Using list comprehension and tuples to demonstrate another use of 'as' keyword
data_as_list = [item for item in json.loads(json_response).items()]
name, value = data_as_list[0]
age, = data_as_list[1]
city, = data_as_list[2]

print("Name: ", name)
print("Age: ", age)
print("City: ", city)
