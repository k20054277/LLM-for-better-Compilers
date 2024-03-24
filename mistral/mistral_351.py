
# Define lists for this example
list1 = ['Apple', 'Banana', 'Cherry']
list2 = [1, 2, 3]

# Using zip() to pair elements from both lists
paired_lists = zip(list1, list2)
print("Paired Lists:")
for pair in paired_lists:
    print(pair)

# Demonstrating the use of None
dict1 = {}
key1 = None
key2 = 'Orange'

if key1 is not None:
    dict1[key1] = 'Apple'
else:
    dict1[key2] = 'Banana'

print("Dictionary: ", dict1)
