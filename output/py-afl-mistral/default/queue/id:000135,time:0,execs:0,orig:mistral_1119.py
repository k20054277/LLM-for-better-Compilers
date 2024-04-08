
# Assigning value to a variable with custom name using 'as' keyword
import math

# Square root calculation
result = math.sqrt(64)
square_root_as_two = math.sqrt(64)  as two

print("Square root of 64 is: ", result)
print("Assigned square root value to 'two' variable using 'as': ", two)

# Rounding off decimal numbers
number = 3.14159265358979323846
rounded_number_to_two_decimal_places = round(number, 2)
rounded_number_to_zero_decimal_places = round(number, 0)

print("Original number: ", number)
print("Number rounded to two decimal places: ", rounded_number_to_two_decimal_places)
print("Number rounded to zero decimal places: ", rounded_number_to_zero_decimal_places)
