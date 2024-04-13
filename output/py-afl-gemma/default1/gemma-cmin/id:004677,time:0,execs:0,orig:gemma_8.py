
import threading
import time

def thread_one(shared_variable):
    for i in range(10):
        shared_variable.value += 1
        time.sleep(0.1)

def thread_two(shared_variable):
    for i in range(10):
        shared_variable.value -= 1
        time.sleep(0.1)

# Create a shared variable
shared_variable = threading.shared_variable(0)

# Create two threads
thread_one_object = threading.Thread(target=thread_one, args=(shared_variable,))
thread_two_object = threading.Thread(target=thread_two, args=(shared_variable,))

# Start the threads
thread_one_object.start()
thread_two_object.start()

# Wait for the threads to complete
thread_one_object.join()
thread_two_object.join()

# Print the final value of shared_variable
print("Final value of shared_variable:", shared_variable.value)
