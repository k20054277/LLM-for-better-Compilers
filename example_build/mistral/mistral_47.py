
# False example
x = 0
if x:
    print("x is truthy (non-zero)")
else:
    print("x is falsy (zero or None)")
print(not x) # prints "True"
