
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use a for loop to check if each number is greater than 3
# If it is, print the number and use the Boolean value True
for num in numbers:
    if num > 3:
        print(num, "is greater than 3. ", True)
    else:
        print(num, "is less than or equal to 3.")

# Use a variable to store a Boolean value
is_sunny = True

# Print the message based on the Boolean value
if is_sunny:
    print("It's sunny outside!")
else:
    print("It's not sunny outside :(")
