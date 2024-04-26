
import threading
import time

def my_function(condition):
    while condition:
        print("Thread is running...")
        time.sleep(1)
        if not condition:
            break

condition = True

thread = threading.Thread(target=my_function, args=(condition,))
thread.start()

# Main thread work
print("Main thread is working...")
time.sleep(3)
condition = False

print("Setting condition to False in main thread.")
