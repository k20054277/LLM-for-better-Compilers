import threading

def print_true():
    print("True")

def print_false():
    print("False")

if __name__ == "__main__":
    t1 = threading.Thread(target=print_true)
    t2 = threading.Thread(target=print_false)
    t1.start()
    t2.start()