
# Initialize a variable with a value less than 10
num = 5

# Use while loop to count numbers from 0 to 9 (including current number)
while num <= 9:
    print(num)
    num += 1

# Print a message when the condition is no longer met
print("The counting has reached 10.")

# Set a boolean variable to True and use while loop to demonstrate its usage
is_even = True
number = 0

while is_even:
    print(number)
    number += 2
    if number > 10:
        is_even = False
