def check_false(x):
    if not isinstance(x, bool):
        return False
    elif x == False:
        return True
    else:
        return False

print(check_false(False)) # Should print "True"
print(check_false(True)) # Should print "False"
print(check_false("hello")) # Should print "False"