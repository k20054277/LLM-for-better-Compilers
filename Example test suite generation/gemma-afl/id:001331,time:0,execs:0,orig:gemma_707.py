
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load sample data
df = pd.DataFrame({
    "name": ["John Doe", "Jane Doe", "Peter Pan"],
    "age": [25, 30, 12],
    "sex": ["male", "female", "male"]
})

# Create a scatterplot
sns.scatterplot(x="age", y="name", data=df)

# Add a hue parameter for the sex column
sns.scatterplot(x="age", y="name", hue="sex", data=df)

# Show the plot
plt.show()
