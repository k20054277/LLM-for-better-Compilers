
numbers = [1, 2, 3, 4, 5, 6]

# Using 'and' for logical operations
found_element = False
for num in numbers:
    if num < 0 and num % 2 == 0: # condition1 (less than zero) and condition2 (even number)
        found_element = True
        print(f"Found an element {num} which is less than 0 and even.")
        break
if not found_element:
    print("No such element exists in the list.")
