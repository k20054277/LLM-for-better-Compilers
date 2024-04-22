
# Iterating through pairs in a list of tuples using 'as' and 'in'
data = [(1, "one"), (2, "two"), (3, "three")]
for i, name in data as item:  # Assigning the tuple values to 'i' and 'name' with 'as'
    print(f"{i} is named {name}")
