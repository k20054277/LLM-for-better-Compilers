
# List of strings
my_list = ['apple', 'banana', '', 'orange']

# Condition with and and len()
if not (len(my_list) < 2 and my_list[-1] == ''):
    print("The list has more than one item and the last item is not empty.")
else:
    print("The list has less than two items or the last item is empty.")

# Output: The list has less than two items or the last item is empty.
