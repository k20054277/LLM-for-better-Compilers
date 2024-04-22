
# An empty list to store boolean values
my_list = []

# Adding some false values to the list
my_list.append(False)
my_list.append(0)
my_list.append("")
my_list.append(None)

print("List before checking for falsiness:")
print(my_list)

# Checking if each value in the list is false using a for loop and an if statement
for value in my_list:
    if not value:
        print(f"Value '{value}' is considered False.")

print("\nList after checking for falsiness:")
print(my_list)
