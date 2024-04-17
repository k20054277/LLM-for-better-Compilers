import threading

def my_function(name):
    print("Hello, " + name)

thread1 = threading.Thread(target=my_function, args=("Alice",))
thread2 = threading.Thread(target=my_function, args=("Bob",))

thread1.start()
thread2.start()