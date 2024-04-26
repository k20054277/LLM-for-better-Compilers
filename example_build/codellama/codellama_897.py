# Create two lists with different lengths
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8, 9]

# Use zip to iterate over both lists simultaneously
for a, b in zip(list1, list2):
    # Check if the elements are equal using and
    if a == b:
        print("The elements are equal")
    else:
        print("The elements are not equal")