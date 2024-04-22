
# Assigning a list alias using the 'as' keyword
numbers = [1, 2, 3, 4, 5]
squared_numbers as squares = [i**2 for i in numbers]
print(squares)  # [1, 4, 9, 16, 25]
