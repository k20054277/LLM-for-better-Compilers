
# This variable will have a value of False
boolean_variable = False

# The 'not' operator can be used to negate the boolean value
negated_boolean = not boolean_variable
print("The negated boolean value is:", negated_boolean)

# The 'abs()' function is used to get the absolute value of a number
number = -5
absolute_value = abs(number)
print("The absolute value of", number, "is:", absolute_value)

# We can combine these concepts and create more complex expressions
# For example, let's check if a given number is positive or not
number = 3
if number < 0:
    print(number, "is negative")
else:
    print(number, "is positive or zero")
    
# Now we will use the negated boolean and absolute value to make it negative
number = -abs(number)
print("The number with its absolute value made positive and then negated is:", number)
