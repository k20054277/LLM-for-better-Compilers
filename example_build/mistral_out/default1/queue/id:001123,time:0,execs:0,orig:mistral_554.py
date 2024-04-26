
# Define a boolean variable 'is_raining' with a default value of False
is_raining = False

# Ask user if it's raining and update the value of 'is_raining' accordingly
user_input = input("Is it raining? (y/n): ")
if user_input.lower() == "y":
    is_raining = True

# Define a floating-point number 'temperature'
temperature = 25.5

# Print the value of 'is_raining' and 'temperature'
print(f"Is it raining? {is_raining}")
print(f"The current temperature is: {temperature} degrees Celsius")
