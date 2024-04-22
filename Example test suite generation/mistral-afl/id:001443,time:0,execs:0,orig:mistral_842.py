
# Define the list of numbers with their flags (odd or even)
numbers = [(2, True), (3, False), (5, True), (1, False), (6, True)]

# Filter out the numbers that are odd and have an even flag
filtered_numbers = filter(lambda x: x[0] % 2 == 0 and x[1], numbers)

# Convert the result to a list since filter returns an iterator
filtered_numbers = list(filtered_numbers)

print("Filtered Numbers:")
for number in filtered_numbers:
    print(number[0])

# And operator demonstration without using filter
even_odd, is_even = 7, True
if even_odd % 2 == 0 and is_even:
    print("7 is an even number")
else:
    print("7 is an odd number")
