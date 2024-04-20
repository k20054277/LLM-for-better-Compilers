try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("This will always be printed, regardless of the exception")