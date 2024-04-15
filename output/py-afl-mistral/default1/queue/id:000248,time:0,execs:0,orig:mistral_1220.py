
import numpy as np
import pandas as pd

# Assigning large NumPy array using 'as' keyword
arr = np.zeros((1000, 1000)) as large_arr

# Assigning Pandas DataFrame using 'as' keyword
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'b', 'c', 'd', 'e'], columns=list('XYZ')) as my_dataframe

print("Large NumPy array shape: ", large_arr.shape)
print("\nPandas DataFrame Head:")
print(my_dataframe.head())
