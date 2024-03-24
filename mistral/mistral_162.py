
# This variable 'is_raining' is assigned False value since it represents a condition when it is not raining
is_raining = False

# In this example, we use comparison operators (<, >, ==, !=) to create expressions that evaluate to True or False
# Based on the current state of 'is_raining' variable, these expressions will return different results
print("Is it raining?", is_raining)
print("Does 5 come before 10?", 5 < 10)
print("Are 2 and 3 equal?", 2 == 3)
print("Is False value greater than True?", False > True)

# We can also combine expressions using logical operators (and, or, not)
# 'and' returns True if both expressions are True. 'or' returns True if at least one expression is True. 'not' negates the result of an expression.
print("Is it raining and 2 equals 3?", is_raining and 2 == 3)
print("Does it rain or is 2 equal to 3?", is_raining or 2 == 3)
print("Is it not raining?", not is_raining)
