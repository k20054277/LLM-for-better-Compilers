
# Creating an empty set
my_set = set()

# Adding elements to the set
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.update([4, 5, 6])

print("My Set: ", my_set)

# Using None as a value
none = None
number = 5
if number is None:
    print("Number is None")
else:
    print(f"Number is {number}")
    
# Using None as a key in a dictionary
my_dict = {"key1": "value1", "key2": "value2", None: "none_value"}
print("My Dictionary: ", my_dict)
