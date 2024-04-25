
import threading

# Define a class to demonstrate as and deadlock
class MyClass(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name)
        self.flag = False

    def run(self):
        # Wait for the other thread to set the flag
        while not self.flag:
            pass

        # Set the flag to True
        self.flag = True

# Create two threads
thread1 = MyClass("Thread 1")
thread2 = MyClass("Thread 2")

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to complete
thread1.join()
thread2.join()

# Print the result
print("The threads have completed.")
