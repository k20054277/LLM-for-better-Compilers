global_variable = 10

def my_function():
    global global_variable
    print("Inside function")
    global_variable += 1
    print(global_variable)

my_function()
print(global_variable)