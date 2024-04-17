
# List of some values
data = [1, "apple", 3.14, "banana", 5]

# Using a for loop with enumerate() to iterate over the list and check if each element is false
for index, value in enumerate(data):
    if not value:
        print(f"The item at index {index} is false: {value}")
    else:
        print(f"The item at index {index} is truthful: {value}")
