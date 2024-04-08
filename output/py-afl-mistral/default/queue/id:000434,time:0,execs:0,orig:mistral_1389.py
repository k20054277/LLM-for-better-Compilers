
import pickle

def validate_input(input_data):
    assert isinstance(input_data, dict), "Input must be a dictionary"
    assert all(isinstance(value, (int, float)) or isinstance(value, str) for key, value in input_data.items()), \
        "Values in the dictionary must be either int, float or str"

data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

validate_input(data)

# Serialize data using pickle
output_file = open('data.pickle', 'wb')
pickle.dump(data, output_file)
output_file.close()

print("Data serialized successfully")

# Deserialize data from pickle
input_file = open('data.pickle', 'rb')
deserialized_data = pickle.load(input_file)
input_file.close()

validate_input(deserialized_data)
print("Data deserialized successfully")

print("Deserialized data: ", deserialized_data)
