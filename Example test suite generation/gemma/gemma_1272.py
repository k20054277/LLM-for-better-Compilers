
import threading
import time

def race_condition(n):
    global shared_variable
    for _ in range(n):
        shared_variable += 1

shared_variable = 0

threads = []
for i in range(10):
    thread = threading.Thread(target=race_condition, args=(i,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Final value of shared_variable:", shared_variable)
