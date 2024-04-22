
# Assign values to variables
x = True
y = False

# Use 'and' operator with 'as' keyword for assignment
a, b = x and True if x else False, y and not False or True

# Print the values of variables 'a' and 'b'
print("Value of variable 'a':", a)
print("Value of variable 'b':", b)

# Explanation:
# In the first assignment with 'and' operator, 'True and True' evaluates to 'True'. Since the condition is met, the right side of the assignment is executed which assigns 'True' to 'a'. On the other hand, 'False and False' evaluates to 'False', so 'False' is assigned to 'b'.
# In the second assignment with 'and' operator and 'not' keyword, 'False and not False' evaluates to 'False' since 'not False' is 'True'. Since the condition is not met, 'False' is assigned to 'a' and 'True' (which was the result of 'not False') is assigned to 'b'.
# In the third assignment with 'or' operator and 'not', 'False and not True' evaluates to 'False'. However, since at least one condition needs to be true for 'or' operator, 'True' (which is the second part of the right side) is assigned to 'b'. 'False' is assigned to 'a'.
