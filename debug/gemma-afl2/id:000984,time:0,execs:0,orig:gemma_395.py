
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data
x = [i for i in range(10)]
y = [i**2 for i in x]

# Create a scatterplot
sns.scatterplot(x, y)

# Add a linear regression line
sns.regplot(x, y)

# Show the plot
plt.show()
