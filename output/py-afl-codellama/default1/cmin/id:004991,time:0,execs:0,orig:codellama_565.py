import threading

# Create a shared variable to store the current value of the counter
counter = 0

# Define a function that will be executed by each thread
def increment_counter():
    # Lock the mutex before accessing the shared variable
    with lock:
        # Increment the counter
        counter += 1

# Create a list of threads to run the function
threads = []
for i in range(5):
    t = threading.Thread(target=increment_counter)
    threads.append(t)

# Start the threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("Final value of counter:", counter)