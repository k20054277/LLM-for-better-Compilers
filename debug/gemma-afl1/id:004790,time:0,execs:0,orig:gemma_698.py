
import pickle

# Define a function to demonstrate True and pickle
def demonstrate_true_and_pickle():
    # Create a dictionary
    my_dict = {"key1": True, "key2": 10, "key3": "Hello, world!"}

    # Pickle the dictionary
    with open("my_dict.pkl", "wb") as f:
        pickle.dump(my_dict, f)

    # Unpickle the dictionary
    with open("my_dict.pkl", "rb") as f:
        unpickled_dict = pickle.load(f)

    # Print the unpickled dictionary
    print(unpickled_dict)

# Call the function
demonstrate_true_and_pickle()
