
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Generate random data using NumPy
np.random.seed(42)  # for reproducibility
data = np.random.randn(100, 2)

# Create a simple line plot using Seaborn
sns.set()
fig, ax = plt.subplots(figsize=(8, 6))
sns.lineplot(x=data[:, 0], y=data[:, 1], ax=ax)
sns.kdeplot(data[:, 0], data[:, 1], shade=True, color="grey", label="Density")
ax.set_title("Scatter plot with KDE Density Estimation")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.legend()
plt.show()

# Create a joint-histogram using Seaborn
fig, ax = plt.subplots(figsize=(8, 6))
sns.jointplot(data[:, 0], data[:, 1], color="grey", kde=True)
ax.set_title("Joint Histogram with KDE Density Estimation")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()
