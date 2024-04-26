
x, y = 10, 3
q, r = divmod(x, y)
print("Quotient:", q)
print("Remainder:", r)

# Using as for aliasing
q, r = divmod(x, y)
a, b = q, r
print("Quotient using alias a:", a)
print("Remainder using alias b:", b)
