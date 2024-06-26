import seaborn as sns

# Generate some random data
data = pd.DataFrame({'x': np.linspace(0, 10, 50), 'y': np.random.normal(size=50)})

# Create a line plot using Seaborn
sns.lineplot(x='x', y='y', data=data)

# Add a title and label the axes
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()