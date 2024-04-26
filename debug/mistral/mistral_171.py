
# Define a boolean variable with a false value
is_raining = False

print("Is it raining? ", is_raining)

# Negation operation: change the boolean value to true
is_sunny = not is_raining

print("Is it sunny? ", is_sunny)

# Conditional statements using false and negation
if not is_raining:
    print("You don't need an umbrella!")
else:
    print("You will get wet in the rain. Remember to take an umbrella.")

# Another example of conditional statement
if not (is_raining and is_sunny):
    print("It's either raining or it's not sunny today!")
