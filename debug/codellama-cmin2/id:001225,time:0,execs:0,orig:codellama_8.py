# This program demonstrates the use of True and deadlock in Python

import threading

def worker():
  # Do some work
  print("Worker thread")

def main():
  # Create a new thread
  t = threading.Thread(target=worker)

  # Start the thread
  t.start()

  # Wait for the thread to finish
  t.join()

if __name__ == "__main__":
  main()