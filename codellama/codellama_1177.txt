import threading

def do_something(x, y):
    # Do something with x and y
    print("Doing something with", x, "and", y)

# Create two threads
t1 = threading.Thread(target=do_something, args=(5, 10))
t2 = threading.Thread(target=do_something, args=(15, 20))

# Start the threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()