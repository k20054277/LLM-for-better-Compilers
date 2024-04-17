
# Using range() function to generate a sequence of numbers and iterate through it using for loop
for i in range(5):
    print("Number is: ", i)

# Now, let's use as keyword with range() function to assign the name to each iteration value
for number in (i for i in range(5)):
    print("Number is: ", number)

# Output:
# Number is: 0
# Number is: 1
# Number is: 2
# Number is: 3
# Number is: 4
