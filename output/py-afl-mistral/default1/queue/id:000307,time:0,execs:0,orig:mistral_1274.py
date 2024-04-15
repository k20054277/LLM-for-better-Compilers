
# Using 'as' keyword to assign aliases
import shlex as Lex # Importing shlex module and aliasing it as 'Lex'

original_string = "hello world"
string_list, extension = Lex.split(original_string) # Splitting a string into list using 'shlex.split()'
print("String: ", original_string)
print("List: ", list)
print("Extension: ", extension)

# Using ',' for multiple assignments in one line
x, y = 10, 20 # Assigning values to x and y variables
z = x + y
print("x: ", x)
print("y: ", y)
print("z: ", z)
