
import threading
import time

# Define a shared variable
shared_variable = 0

# Define two threads
thread1 = threading.Thread(target=lambda:
    for i in range(10):
        shared_variable += 1
        time.sleep(0.1)
)

thread2 = threading.Thread(target=lambda:
    for i in range(10):
        shared_variable -= 1
        time.sleep(0.1)
)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to complete
thread1.join()
thread2.join()

# Print the final value of shared_variable
print(shared_variable)
