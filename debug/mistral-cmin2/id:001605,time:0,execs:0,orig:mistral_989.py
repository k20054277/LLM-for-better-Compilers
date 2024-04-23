
# script_A.py
import threading
import time

shared_variable = 0

def function_A():
    global shared_variable
    print("Thread A started")
    for i in range(1000):
        shared_variable += 1
    print("Thread A finished")

thread_A = threading.Thread(target=function_A)
thread_A.start()
thread_A.join()

def function_B():
    global shared_variable
    print("Thread B started")
    for i in range(1000):
        shared_variable += 1
    print("Thread B finished")

thread_B = threading.Thread(target=function_B)
thread_B.start()
thread_B.join()

print(f"The final value of the shared variable is: {shared_variable}")
