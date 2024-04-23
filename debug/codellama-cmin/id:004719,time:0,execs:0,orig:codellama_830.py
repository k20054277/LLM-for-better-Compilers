# This program demonstrates the use of "and" and "global" in Python

def is_positive(x):
    global result
    if x > 0:
        result = True
    else:
        result = False
    return result

result = False

print(is_positive(5))   # Should print "True"
print(result)          # Should print "True"

result = False
print(is_positive(-1))  # Should print "False"
print(result)          # Should print "False"