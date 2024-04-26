import threading
import time

def my_function(my_list):
    for i in range(5):
        print("Thread {} says: {}".format(threading.current_thread().name, my_list[i]))

my_list = ["Hello", "World", "Python", "Threads"]

t1 = threading.Thread(target=my_function, args=(my_list,))
t2 = threading.Thread(target=my_function, args=(my_list,))

t1.start()
t2.start()

time.sleep(5)

print("Main Thread says: {}".format(my_list[0]))