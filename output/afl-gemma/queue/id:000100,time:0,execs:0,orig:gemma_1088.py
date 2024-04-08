
# Import the as keyword to give a different name to the module
import random as r

# Use the imported module
print(r.randint(1, 10))

# Import the entire module
import random

# Use the functions and variables from the imported module
print(random.randint(1, 10))
print(random.choice(["a", "b", "c"]))
