
def safe_divide(arg1, arg2):
    if not (isinstance(arg1, (int, float)) and isinstance(arg2, (int, float))):
        print("Error: One or both arguments are not numbers")
        return None
     result = arg1 / arg2
     return result

# Test cases
result1 = safe_divide(5, 3)
print(f"Result of safe_divide(5, 3): {result1}") # Expected output: Result of safe_divide(5, 3): 1.6666666666666667

result2 = safe_divide("a", 3)
print(f"Result of safe_divide(\"a\", 3): {result2}") # Expected output: Error: One or both arguments are not numbers

# Else block example
def safe_divide_else(arg1, arg2):
    if not (isinstance(arg1, (int, float)) and isinstance(arg2, (int, float))):
        print("Error: One or both arguments are not numbers")
        return None
     result = arg1 / arg2
     else:
         print(f"Result of safe_divide({arg1}, {arg2}): {result}") # This will be executed if the condition in 'if' is False.
