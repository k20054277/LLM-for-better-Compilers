import seaborn as sns
import matplotlib.pyplot as plt

# Generate some random data
data = {'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 40, 50]}

# Create a bar chart using seaborn
sns.barplot(x='x', y='y', data=data)

# Show the plot
plt.show()