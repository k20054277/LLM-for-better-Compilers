
# Assigning False directly
is_raining = False
print("Is it raining? ", is_raining)

# Comparison with numbers
zero = 0
negative_number = -1

if zero > False or negative_number < False:
    print("The comparison results in True")
else:
    print("The comparison results in False")

# Comparison with strings and other Boolean values
empty_string = ""
another_boolean = True

if empty_string == False or another_boolean is False:
    print("Both conditions are equivalent to True")
else:
    print("One of the conditions is False")
