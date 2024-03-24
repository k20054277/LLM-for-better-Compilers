
# Initialize a variable with a value that is initially considered true for the loop condition
my_number = 10

# Use while loop to continue executing the block as long as my_number is greater than zero (which is considered true)
while my_number > 0:
    print(my_number)

    # Decrease the value of my_number by one at each iteration
    my_number -= 1

# Now, my_number has become false (zero), and the loop ends
print("The number is no longer greater than zero, so the loop finishes.")
