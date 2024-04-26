
# Initialize some variables with None value
data = None
numbers = None

print("Initial values:")
print("Data:", data)
print("Numbers:", numbers)

# Using a for loop to iterate over an empty list and assign None to each element
numbers = []
for i in range(5):
    numbers.append(None)

print("\nAssigned None to each element of the list:")
print("Numbers:", numbers)

# Using a for loop with data variable and checking if it is None
data = 10
print("\nData now has a value, let's check if the variable 'data' is None:")
for i in range(3):
    if data is None:
        print("Data is still None!")
        break
    print("Data is not None.")

# Now set Data to None again and checking if it is equal to any number
print("\nChecking 'data' against numbers using 'is':")
for num in [1, 2, 3, 4]:
    if data is num:
        print(f"Data is the same as number {num}!")
        break
    print(f"Data is not the same as number {num}.")

print("\nChecking 'data' against numbers using '==':")
for num in [1, 2, 3, 4]:
    if data == num:
        print(f"Data is equal to number {num}!")
        break
    print(f"Data is not equal to number {num}.")
