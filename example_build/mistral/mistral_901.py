
import pickle

# Define some data
data = {
    "name": "John Doe",
    "age": 30,
    "is_student": True
}

# Define a function that checks if person is student and above 18
def check_eligibility(person):
    return person["is_student"] and person["age"] > 18

# Check eligibility of data
if check_eligibility(data):
    print("The person is eligible.")
else:
    print("The person is not eligible.")

# Pickle the data
with open("data.pickle", "wb") as f:
    pickle.dump(data, f)

# Load pickled data
with open("data.pickle", "rb") as f:
    loaded_data = pickle.load(f)

# Check eligibility of loaded data
if check_eligibility(loaded_data):
    print("The loaded person is eligible.")
else:
    print("The loaded person is not eligible.")
