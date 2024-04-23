
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate some random data with outliers
np.random.seed(0)  # for reproducibility
data = np.random.randn(100, 2)
outliers = np.random.choice(len(data), size=10, replace=False)
outliers_data = data[outliers] * 3
data = np.concatenate((data, outliers_data))

# Use NumPy's True to create a boolean mask for the outlier indices
is_outlier = np.isin(np.arange(len(data)), outliers)

# Create a scatter plot with Seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(x=data[:, 0], y=data[:, 1], hue=is_outlier, s=50, palette="Set3")

# Set axis labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter plot with outliers")

# Show the plot
plt.show()
