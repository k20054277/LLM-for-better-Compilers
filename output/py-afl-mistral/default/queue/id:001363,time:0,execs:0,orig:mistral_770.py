
# Initialize the counter variable with a value of 0
counter = 0

# Use an infinite loop and include a condition to break the loop using 'True' and 'while'
while True:
    # Check if the counter is greater than 9 using the modulus operator '%'
    if counter > 9:
        # If the condition is true, then break out of the loop using 'break' statement
        break

    # Print the current value of the counter and its square
    print("Counter: {0} \nSquare: {1}")
    print(counter * counter)

    # Increment the counter using modulus operator '%=' to ensure that it stays within the range of 0 to 9
    counter += 1
    counter %= 10
