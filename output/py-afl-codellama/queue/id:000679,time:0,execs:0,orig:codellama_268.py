# Iteration with False
def iterate_false(n):
    i = 0
    while i < n:
        print("Iteration:", i)
        i += 1
        if i == 5:
            return False
    return True

print(iterate_false(10)) # Should print "False"