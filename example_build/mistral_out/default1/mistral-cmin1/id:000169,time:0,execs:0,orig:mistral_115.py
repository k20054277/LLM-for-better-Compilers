
import pickle

# Demonstrating False value
bool_values = [True, False]
print("Boolean values: ", bool_values)

# Demonstrating pickle module with a dictionary containing a boolean value
my_dict = {
    "name": "John Doe",
    "is_student": False
}

print("\nMy dictionary: ", my_dict)

# Serializing (pickling) the dictionary using pickle
with open("my_dict.pkl", "wb") as file:
    pickle.dump(my_dict, file)

print("\nDictionary pickled successfully.")

# Deserializing (unpickling) the dictionary from pickle
with open("my_dict.pkl", "rb") as file:
    loaded_dict = pickle.load(file)

print("\nLoaded dictionary: ", loaded_dict)
