
# Importing modules using as
import math as m

print(m.sqrt(16))  # prints 4.0

# Renaming variables with as
a = [1, 2, 3]
b = [4, 5, 6]
c = a  # creates a reference to the same list
a = [7, 8, 9]  # modifies the original list
print(c)  # prints: [1, 2, 3]

a as b  # SyntaxError: 'as' expected an assignment or import statement
# Corrected version:
a = [7, 8, 9]
b = a
c = a
a = [0, 0, 0]  # modifies the original list 'b' now
print(b)  # prints: [7, 8, 9]
print(c)  # prints: [7, 8, 9]
