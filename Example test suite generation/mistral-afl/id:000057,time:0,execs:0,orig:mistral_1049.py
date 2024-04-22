
# Function that calculates the square of a number
def square(num):
    squared = num ** 2
    return squared

# Global variable
num = 5

# Local function call that squares a global variable using 'global' keyword
def square_global():
    global num
    result = square(num)
    print("Square of global num: ", result)
    num += 1 # modifying global variable directly
    print("Updated global num: ", num)

# Local function call that squares a local variable using 'as' keyword
def square_local():
    num = 7
    squared = (square(num) if num > 0 else None) # calculating square only if num is positive
    result = squared if result else "Error: Invalid number"
    print("Square of local num: ", result)

# Function calls
square_global()
square_local()
print("Global num after function calls: ", num)
