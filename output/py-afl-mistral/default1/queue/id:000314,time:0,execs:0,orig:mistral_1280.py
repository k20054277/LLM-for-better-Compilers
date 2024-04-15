
# Using 'as' keyword to assign aliases
import numpy as np
import pandas as pd

# Create a NumPy array using 'as' keyword
nd_array = np.array([1, 2, 3, 4, 5], dtype=np.int32) as nd_arr

# Using 'as' keyword to assign aliases to columns in a DataFrame
data = {'Name': ['John', 'Mike', 'Sara'], 'Age': [27, 30, 34]}
df = pd.DataFrame(data)
columns = df.columns.tolist() as cols

print("NumPy array using alias:")
print(nd_arr)
print("Columns in DataFrame using alias:")
print(cols)

# Using ';' keyword to separate multiple statements on the same line
x = 5; y = 10; print(x, y)
