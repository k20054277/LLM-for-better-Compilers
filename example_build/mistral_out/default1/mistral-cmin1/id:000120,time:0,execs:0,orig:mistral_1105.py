
# List of tuples, each containing a name and an age
data = [("Alice", 25), ("Bob", 30), ("Charlie", 21)]

# Use max() function with a key function to find the person with maximum age
max_age_person = max(data, key=lambda x: x[1])

print("The person with the maximum age is:", max_age_person[0])
print("Maximum age is:", max_age_person[1])

# Assign aliases to elements in max_age_person using as keyword
name, age = max_age_person

print("Person with maximum age in a more readable way:")
print(f"Name: {name}")
print(f"Age: {age}")
