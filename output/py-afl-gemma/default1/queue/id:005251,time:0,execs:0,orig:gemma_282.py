
# This Python program demonstrates the use of False and continue

for num in range(10):
    if num % 2 == 0 and num % 3 == 0:
        continue
    print(num)

# Output:
# 1
# 2
# 4
# 5
# 7
# 8
# 9
