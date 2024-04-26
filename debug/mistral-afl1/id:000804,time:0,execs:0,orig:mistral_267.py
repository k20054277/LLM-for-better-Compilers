
# A simple list of mixed data types with some elements as None
my_list = [1, "apple", 3.14, None, 5, "orange"]

print("Original List:")
print(my_list)

# Using for loop to iterate over the list and print each element
print("\nPrinting all elements in the list:")
for i in my_list:
    if i is not None:
        print(i)
    else:
        print("None")
