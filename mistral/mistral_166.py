
# Comparison example:
number1 = 5
number2 = 3
if number1 != number2:
    print("The numbers are different")
else:
    print("The numbers are equal") # This won't be printed

# Emptiness check examples:
empty_string = ""
empty_list = []
empty_tuple = ()
if not empty_string:
    print("Empty string is true") # This won't be printed
if len(empty_list) == 0:
    print("Empty list is true") # This will be printed
