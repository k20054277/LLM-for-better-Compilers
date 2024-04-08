# Python Program to demonstrate the use of as and while

# Initialize i with 10
i = 10

# Initialize j with 20
j = 20

# Use while loop to iterate from i to j
while i <= j:
    # Print i
    print(i)
    
    # Increment i by 1
    i += 1

# Use as keyword to assign j to i
i = j as i

# Print i again
print(i)