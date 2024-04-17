
def greet(is_morning=False):
  if is_morning:
    print("Good morning!")
  else:
    print("Hello!")

greet()                     # prints "Hello!"
greet(True)                 # prints "Good morning!"
greet(False)                # prints "Hello!"
