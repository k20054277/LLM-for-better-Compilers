import threading

def task1():
    print("Task 1 started")
    while True:
        if not False:
            print("Task 1 finished")
            break

def task2():
    print("Task 2 started")
    while True:
        if not False:
            print("Task 2 finished")
            break

# Create a new thread for each task
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start the threads
thread1.start()
thread2.start()

# Join the threads (wait for them to finish)
thread1.join()
thread2.join()