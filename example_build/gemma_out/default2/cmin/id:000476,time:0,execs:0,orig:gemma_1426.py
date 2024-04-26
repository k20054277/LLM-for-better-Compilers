
import pickle

# Define a function to demonstrate assert and pickle
def demonstrate_assert_and_pickle():
    # Assert a condition
    assert 5 > 3

    # Pickle an object
    my_object = {"name": "John Doe", "age": 30}
    pickle.dump(my_object, "my_object.pkl")

    # Unpickle an object
    unpickled_object = pickle.load("my_object.pkl")

    # Print the unpickled object
    print(unpickled_object)

# Call the function
demonstrate_assert_and_pickle()
