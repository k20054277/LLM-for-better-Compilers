import threading

# Semaphore for controlling access to shared resources
sem = threading.Semaphore(1)

def critical_section():
    # Acquire semaphore before entering critical section
    sem.acquire()
    
    # Do something with shared resource
    print("Critical section executed")
    
    # Release semaphore after exiting critical section
    sem.release()

# Function to be executed by threads
def thread_function():
    # Loop until program is terminated
    while True:
        # Check if critical section can be entered
        assert sem.acquire(False)
        
        # Enter critical section and perform operation
        critical_section()
        
        # Exit critical section
        sem.release()
        
# Create threads
threads = []
for i in range(5):
    t = threading.Thread(target=thread_function)
    threads.append(t)
    t.start()

# Join threads
for t in threads:
    t.join()