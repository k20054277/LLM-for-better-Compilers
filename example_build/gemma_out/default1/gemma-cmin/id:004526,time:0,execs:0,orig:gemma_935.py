
import pickle

# Create a dictionary
my_dict = {"name": "John Doe", "age": 30, " hobbies": ["reading", "writing", "hiking"]}

# Dump the dictionary to a file
with open("my_dict.pkl", "wb") as f:
    pickle.dump(my_dict, f)

# Load the dictionary from the file
with open("my_dict.pkl", "rb") as f:
    loaded_dict = pickle.load(f)

# Print the loaded dictionary
print(loaded_dict)
