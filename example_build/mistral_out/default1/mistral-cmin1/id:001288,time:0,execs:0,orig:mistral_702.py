
import threading

def print_numbers():
    """Print numbers from 1 to 5"""
    for i in range(1, 6):
        print("Thread-1: ", i)

def print_letters():
    """Print letters a to e"""
    for letter in "abcde":
        print("Thread-2: ", letter)

if __name__ == "__main__":
    # Create threads
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for threads to finish before exiting the program
    thread1.join()
    thread2.join()

# It's important to note that Python GIL (Global Interpreter Lock) doesn't allow multiple native threads to execute Python code at once,
# so in this example, it might not look like true multithreading as the tasks are being executed serially with some short time gaps between them.
