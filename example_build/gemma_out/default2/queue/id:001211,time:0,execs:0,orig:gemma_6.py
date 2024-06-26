
import threading
import time

def thread_function(name):
    for i in range(10):
        print("Hello, " + name + "!")
        time.sleep(1)

# Create a list of threads
threads = []

# Start a thread for each person
for i in range(5):
    thread = threading.Thread(target=thread_function, args=("Person " + str(i+1)))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads completed!")
