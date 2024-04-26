# Using None as a value
x = 5
y = None
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# Using dict to store values
fruits = {"apple": "red", "banana": "yellow"}
print(fruits["apple"])  # prints "red"
print(fruits["orange"])  # KeyError: 'orange' (since orange is not in the dictionary)