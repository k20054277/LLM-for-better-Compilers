# Using None
print(None)  # Output: None
print("Hello" + None)  # Output: HelloNone
print(None + "World")  # Output: WorldNone
print(None * 3)  # Output: NoneNoneNone

# Using set()
print(set([1, 2, 3]))  # Output: {1, 2, 3}
print(set([4, 5, 6]))  # Output: {4, 5, 6}
print(set([1, 2, 3]) - set([4, 5, 6]))  # Output: {1, 2, 3}
print(set([1, 2, 3]) & set([4, 5, 6]))  # Output: {}