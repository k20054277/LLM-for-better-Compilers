
# Define a variable with a false value
is_raining = False

# Use if statement with False condition
if not is_raining:
    print("It's sunny today. Let's go for a picnic!")
else:
    print("It's raining today. Let's stay at home.")

# Use format() with a false condition in the template string
message = f"The weather is {not is_raining and 'sunny' or 'rainy'}. "
message += "Let's do {0 if not is_raining else 'not'} go for a walk."

print(format(message, locals()))
