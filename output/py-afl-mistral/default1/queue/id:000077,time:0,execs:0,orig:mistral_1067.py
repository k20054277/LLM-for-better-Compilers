
# Using as for assignment with alias
def square(num):
    return num ** 2

numbers = [1, 2, 3, 4, 5]

squared = []
for num in numbers:
    squared.append(square(num) as sq)

print("Numbers and their squares:", numbers)
print("Squared values:", squared)

# Using any() to check if at least one element in an iterable is true
def is_odd(num):
    return num % 2 != 0

numbers = [1, 2, 3, 4, 5]

if any(map(is_odd, numbers)):
    print("At least one odd number exists in the list.")
else:
    print("All numbers are even.")
