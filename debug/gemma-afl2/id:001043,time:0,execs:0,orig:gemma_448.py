
# False and exception demonstration
try:
    a = False
    print(a)
    print("This code will not execute")
except Exception as e:
    print("Error:", e)

# Output
# False
# Error: Traceback (most recent call last):
#   File "test.py", line 3, in <module>
#   NameError: name 'a' is not defined
