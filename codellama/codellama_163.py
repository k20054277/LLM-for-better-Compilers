# Define a variable and assign it to either True or False
my_variable = True
print(my_variable) # Output: True

# You can also use the opposite of True and False as well
if my_variable:
    print("The value is True")
else:
    print("The value is False")

# You can also use Boolean operators to combine conditions
if my_variable == True:
    print("The value is exactly True")
elif my_variable == False:
    print("The value is exactly False")
else:
    print("The value is something else")

# You can also use the not operator to negate a condition
if not my_variable:
    print("The value is False")
else:
    print("The value is True")