# This program demonstrates the use of as and zip

# Create a list of names
names = ["Alice", "Bob", "Charlie"]

# Create a list of ages
ages = [25, 30, 35]

# Use as to create a new list with the names and ages paired together
paired_list = []
for name in names:
    for age in ages:
        paired_list.append((name, age))

print(paired_list)

# Use zip to create a new list with the names and ages paired together
zipped_list = list(zip(names, ages))
print(zipped_list)