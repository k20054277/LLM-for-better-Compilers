
# Assigning a global variable 'flag' initially set to False
flag = False

def my_function():
    # Changing the value of the global 'flag' inside the function
    flag = True

# Checking and printing the initial value of 'flag'
if not flag:  # Using False as a comparison value
    print("Flag is initially set to False")
else:
    print("Flag is initially set to True")
    
# Calling my_function() and checking the updated value of 'flag'
my_function()
if not flag:
    print("Flag remains False after function call")
else:
    print("Flag becomes True after function call")

# Accessing the global 'flag' using globals() dictionary
print(globals()['flag'])
