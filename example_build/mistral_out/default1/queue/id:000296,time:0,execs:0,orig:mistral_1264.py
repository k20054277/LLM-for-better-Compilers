
# Assigning an alias using 'as' keyword
import numpy as np
import pandas as pd

# Using the imported libraries with their aliases
x = np.array([1, 2, 3])
y = np.arange(5)
z = x * y[None, :]

data = {'Name': ['John', 'Mike', 'Bob'],
       'Age': [25, 30, 35]}
df = pd.DataFrame(data)

print("NumPy array:")
print(x * np.ones_like(x))

print("\nPandas DataFrame:")
print(df)
