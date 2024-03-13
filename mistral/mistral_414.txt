
# Assigning None to a variable
my_variable = None
print(type(my_variable))  # <class 'NoneType'>

# Function returning None
def greet():
    print("Hello, World!")
    
# Call the function without return value
greet()
print(greet)  # <function greet at 0x7f98d3b6c120>
print(type(greet))  # <class 'function'>
print(type(greet()) is None)  # True
