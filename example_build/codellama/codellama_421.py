try:
    do_something()
except Exception as e:
    print("An error occurred:", e)
else:
    print("No errors")
finally:
    cleanup()