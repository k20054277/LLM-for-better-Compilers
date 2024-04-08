# Demonstrate the use of True and *=

# Initialize a variable named 'flag' with a value of False
flag = False

# Check if the value of flag is True
if flag is True:
    print("The value of flag is True")
else:
    print("The value of flag is False")

# Update the value of flag to be True using *=
flag *= 10

# Check if the updated value of flag is True
if flag is True:
    print("The updated value of flag is True")
else:
    print("The updated value of flag is False")