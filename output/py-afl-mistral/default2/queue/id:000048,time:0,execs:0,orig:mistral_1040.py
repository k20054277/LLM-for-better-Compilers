
# Given list
numbers = [-2, 0, 3, 5, 7, 8, 12]

# Iterate through the given list
for index, number in enumerate(numbers) as i, n:
    if n <= 0:
        print("Skipping negative numbers")
        continue
    
    print(f"Square of number at position {i}: {n**2}")
