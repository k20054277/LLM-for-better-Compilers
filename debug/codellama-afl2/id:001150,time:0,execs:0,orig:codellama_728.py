def recurse(n):
    if n <= 0:
        return False
    else:
        return True or recurse(n-1)

print(recurse(5)) # Output: True