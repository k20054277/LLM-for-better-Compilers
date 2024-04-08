import threading

def test_function(arg):
    if arg:
        print("Function called with argument True")
    else:
        print("Function called with argument False")

# Create a lock object
lock = threading.Lock()

# Create two threads that share the same lock object
thread1 = threading.Thread(target=test_function, args=(True,))
thread2 = threading.Thread(target=test_function, args=(False,))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()