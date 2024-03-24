# Using and
print("Python" in ["Java", "C++", "Python"])  # Output: True
print("Java" in ["Java", "C++", "Python"])  # Output: True
print("C" in ["Java", "C++", "Python"])     # Output: False

# Using reversed
lst = [1, 2, 3, 4, 5]
for i in reversed(lst):
    print(i)  # Output: 5, 4, 3, 2,