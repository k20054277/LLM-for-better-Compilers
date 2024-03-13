
# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Use the and keyword to check if two elements are in both sets
if 4 in set1 and 5 in set2:
    print("Four and Five are in both sets")

# Create a new set that is the intersection of set1 and set2 using the & operator
intersection = set1 & set2
print("Intersection of set1 and set2:", intersection)

# Use the and keyword to check if an element is in both sets and also greater than 3
if 5 in set1 and 5 in set2 and 5 > 3:
    print("Five is in both sets and is greater than 3")

# Use the sets for membership testing with the in keyword
if 6 in set1 or 7 in set2:
    print("Either six or seven is in one of the sets")
