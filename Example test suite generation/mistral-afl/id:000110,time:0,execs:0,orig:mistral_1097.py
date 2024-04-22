
# Using as keyword for variable renaming in list comprehension
data = [1, 2, 3, 4, 5]
squares = [x * x for x in data as sq]
print(type(sq), squares)

# Using int() function to convert a string or other object to an integer
str_num = "10"
int_num = int(str_num)
print(type(int_num))
