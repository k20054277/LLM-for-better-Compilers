# Print "False" if the first argument is less than the second, otherwise print "True"
def compare_numbers(num1, num2):
    if num1 < num2:
        return False
    else:
        return True

print(compare_numbers(5, 10)) # Should print "False"
print(compare_numbers(10, 5)) # Should print "True"