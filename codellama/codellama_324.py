def is_false(x):
    if x == False:
        return True
    else:
        return False

def recursion(n):
    if n == 0:
        return False
    else:
        return is_false(recursion(n-1))

print(recursion(5)) # should print "False"