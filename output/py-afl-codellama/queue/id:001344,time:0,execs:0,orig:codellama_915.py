import pandas as pd
import seaborn as sns

# create a sample dataset
data = {'A': ['apple', 'banana', 'cherry'],
        'B': ['dog', 'cat', 'mouse'],
        'C': [1, 2, 3],
        'D': [4, 5, 6]}
df = pd.DataFrame(data)

# create a bar plot using seaborn
sns.barplot(x='A', y='B', data=df)