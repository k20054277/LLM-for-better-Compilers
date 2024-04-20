import threading

# Define a function to be executed by the thread
def my_function():
    print("Hello from thread!")

# Create a new thread and start it
t = threading.Thread(target=my_function)
t.start()

# Wait for the thread to finish
t.join()

print("Main thread finished!")