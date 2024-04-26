# This program demonstrates the use of None and iteration in Python

# Iterate over a list using None as the stop condition
my_list = ['apple', 'banana', 'cherry']
for item in my_list:
    print(item)

# Use None to break out of an iteration loop
for i in range(10):
    if i == 5:
        break
    print(i)

# Use None as a value in a dictionary
my_dict = {'apple': 'red', 'banana': 'yellow'}
print(my_dict['apple'])
print(my_dict.get('cherry', None))