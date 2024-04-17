# Using and to perform multiple checks at once
x = 10
if x > 5 and x < 20:
    print("Value is between 5 and 20")
else:
    print("Value is not between 5 and 20")

# Using try to handle exceptions
try:
    f = open("example.txt", "r")
except IOError as e:
    print("Unable to open file. Error: ", e)
finally:
    if f:
        f.close()