x = 5
y = "hello"
print(x and y) # This will print "hello" because "hello" is not a false value
print(y and x) # This will print 5 because 5 is not a false value
print(type(x and y)) # This will print "<class 'str'>" because "hello" is a string
print(type(y and x)) # This will print "<class 'int'>" because 5 is an integer