
# This program checks if two numbers are within a certain range using and operator
def is_within_range(num, start, end):
 """
 :param num: The number to check.
 :param start: The minimum allowed value.
 :param end: The maximum allowed value.
 :return: True if the number is within the given range, False otherwise.
 """
 return start <= num <= end

# This program evaluates a simple arithmetic expression using eval() function
def calculate(expression):
 """
 :param expression: A string representing an arithmetic expression.
 :return: The result of the evaluation.
 """
 result = eval(expression)
 print(f"Result: {result}")
 return result

if __name__ == "__main__":
 # Check if a number is within the range (10, 20) using and operator
 num = int(input("Enter a number: "))
 if is_within_range(num, 10, 20):
 print("The number is within the range.")
 else:
 print("The number is not within the range.")

 # Evaluate an arithmetic expression using eval() function
 expression = input("Enter an arithmetic expression: ")
 calculate(expression)
