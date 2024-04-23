
# This variable will have a value that is deliberately set to False
is_sunny = False

# Let's assume the temperature is -15 degrees Celsius
temperature = -15

def get_message():
 if not is_sunny:
 message = "It's a rainy day. Sadly, I can't go out."
 else:
 message = f"The temperature today is {temperature} degrees Celsius. Let's go out and enjoy!"
 return message

# Get the message based on our conditions
print(get_message()))

# Now let's print the absolute value of the temperature
print("The absolute value of the temperature is:", abs(temperature))
