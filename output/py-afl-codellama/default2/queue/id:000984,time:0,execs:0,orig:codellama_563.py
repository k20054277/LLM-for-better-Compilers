# This code demonstrates the use of None and deadlock in Python

# Creating a thread that will wait for a value to be assigned to x
x = None
t1 = Thread(target=wait_for_value, args=(x,))
t1.start()

# Creating another thread that will assign a value to x after the first thread is waiting
t2 = Thread(target=assign_value, args=(x, 5))
t2.start()

# Waiting for both threads to finish
t1.join()
t2.join()

def wait_for_value(x):
    # This thread will wait indefinitely until a value is assigned to x
    while True:
        if x is not None:
            print("Received value:", x)
            return

def assign_value(x, new_value):
    # This thread will sleep for 5 seconds before assigning a value to x
    time.sleep(5)
    x = new_value