
# Define a global variable 'flag' with an initial value of True
flag = True

def my_function():
    print("Function entered")
    
    # By default, variables inside functions are local
    local_flag = False

    print("Local flag: ", local_flag)
    print("Global flag: ", flag)

    # To modify the global variable 'flag', use the 'global' keyword
    global flag
    flag = not flag

    print("Local flag: ", local_flag)
    print("Global flag: ", flag)

my_function()
print("Global flag after calling my_function(): ", flag)
