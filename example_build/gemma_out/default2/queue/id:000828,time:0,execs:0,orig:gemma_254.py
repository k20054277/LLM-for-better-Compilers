
import pickle

# Create a dictionary
my_dict = {"name": "John Doe", "age": 30, "interests": ["music", "reading", "hiking"]}

# Serialize the dictionary
with open("my_dict.pkl", "wb") as f:
    pickle.dump(my_dict, f)

# Deserialize the dictionary
with open("my_dict.pkl", "rb") as f:
    loaded_dict = pickle.load(f)

# Print the loaded dictionary
print(loaded_dict)
