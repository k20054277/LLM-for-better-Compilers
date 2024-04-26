# Demonstrate the use of None
print("Demonstrating the use of None")

# Create a variable named 'x' with an initial value of 5
x = 5

# Print the value of x
print(f"The value of x is: {x}")

# Assign None to x
x = None

# Print the value of x again
print(f"The value of x after assigning None is: {x}")

# Demonstrate race conditions
print("Demonstrating race conditions")

# Create two threads that will access and modify a shared variable 'y'
def thread_1():
    y += 1

def thread_2():
    y -= 1

# Start the threads
thread_1()
thread_2()

# Print the value of y to show that it has been modified by both threads
print(f"The value of y after modification by two threads is: {y}")