def test(x, y):
    if x > 0 and y > 0:
        return True
    else:
        return False

print(test(-1, -2))   # should print False
print(test(1, 2))     # should print True