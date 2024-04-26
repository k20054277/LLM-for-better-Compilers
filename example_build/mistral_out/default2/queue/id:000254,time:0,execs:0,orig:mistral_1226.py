
import os

# Set an environment variable
os.environ["MY_VAR"] = "This is my value"

# Assign alias to a list using 'as'
numbers = [1, 2, 3, 4, 5]
nums_alias = list(numbers) as num_aliases

print("Environment variable: ", os.environ["MY_VAR"])

print("Original list: ", numbers)
print("List alias: ", num_aliases)

# Modify the list alias and check its impact on the original list
num_aliases[0] = 10
print("Modified list alias: ", num_aliases)
print("Impact on the original list: ", numbers)
