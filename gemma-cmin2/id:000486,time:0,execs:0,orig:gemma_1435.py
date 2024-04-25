
import seaborn as sns
import pandas as pd

# Create a sample dataset
df = pd.DataFrame({"x": [1, 2, 3, 4], "y": [50, 60, 70, 80], "group": ["A", "B", "A", "B"]})

# Plot a boxplot
sns.boxplot(x="group", y="y", data=df)

# Assert that the boxplot has the expected number of outliers
assert sns.count_outliers(x="group", y="y", data=df) == 0

# Print the boxplot
sns.plt.show()
