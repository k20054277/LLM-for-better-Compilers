
# Let's assume we have two lists:
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# First, let's see how to use the 'and' keyword in Python:
# The 'and' keyword returns True only if both expressions are true.
print("List elements are equal using 'and':")
for i in range(len(list1)):
    if list1[i] == list2[i] and list1[i] > 3:
        print(f"Index {i}: List1[{i}] = {list1[i]} is equal to List2[{i}] = {list2[i]} and greater than 3.")

# Now, let's see how to use the 'zip' function:
print("\nList elements paired using 'zip':")
paired_elements = zip(list1, list2)
for pair in paired_elements:
    element1, element2 = pair
    print(f"Index 0: List1[{list1.index(element1)}] = {element1} and List2[{list2.index(element2)}] = {element2}")
