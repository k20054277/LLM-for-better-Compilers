
# Assigning boolean values to variables
is_sunny = False
is_raining = True

print("Is it sunny? ", is_sunny)
print("Is it raining? ", is_raining)

# Using boolean values in expressions and conditions
if not is_sunny:
    print("Take an umbrella, it's raining!")
else:
    print("Enjoy the sunny day!")

# Boolean operators
print(2 > 1 and 3 > 2)  # And operator (both conditions must be true)
print(2 < 1 or 3 > 2)   # Or operator (at least one condition must be true)
print(not(2 > 1))       # Not operator (negates a boolean value)
