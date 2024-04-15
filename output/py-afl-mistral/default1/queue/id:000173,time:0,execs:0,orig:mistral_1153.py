
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate some sample data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'James'],
    'Age': [28, 35, 42, 29, 36],
    'Gender': ['M', 'F', 'M', 'F', 'M']
}

df = pd.DataFrame(data)

# Use as with DataFrame column assignment
df['New_Column'] = df['Age'] * 2
print(df.head())

# Seaborn example using the generated data
sns.set()
fig, ax = plt.subplots(figsize=(10,6))
sns.scatterplot(x='Age', y='New_Column', hue='Gender', data=df)
sns.lineplot(x='Age', y='New_Column', data=df, label='New Column')
ax.set_title('Seaborn Scatterplot with Line')
ax.legend()
plt.show()
