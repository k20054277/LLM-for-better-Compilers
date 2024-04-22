
# Example 1: Assigning an alias using 'as'
import pandas as pd
data = {'Name': ['John', 'Anna', 'Peter'], 'Age': [25, 30, 22]}
df = pd.DataFrame(data)

# Using the alias 'pd' instead of importing pandas every time
df_grouped = df.groupby('Name').mean()
df_grouped.columns = ['Average_Age']

print(df_grouped)

# Example 2: Renaming an imported module or object using 'as'
import numpy as np
x = np.array([1, 2, 3])
y = x * 2
np_sum = np.sum(y)

print('Using NumPy directly:', np.sum(y))
print('Using the alias "np":', np.sum(y) as np_sum_alias)
print('Both results should be the same.')
