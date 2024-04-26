[PYTHON]
# This program demonstrates the use of None and concurrency in Python
import threading

def use_none(my_none):
    if my_none is not None:
        print("None was passed")
    else:
        print("None was not passed")

def main():
    threads = []
    for i in range(2):
        t = threading.Thread(target=use_none, args=(None,))
        threads.append(t)
        t.start()

if __name__ == '__main__':
    main()
[/PYTHON]