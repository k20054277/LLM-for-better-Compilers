# This program will attempt to divide two numbers and catch any errors that occur

try:
  result = num1 / num2
except ZeroDivisionError as e:
  print("You cannot divide by zero!")
  print(e)
else:
  print(result)