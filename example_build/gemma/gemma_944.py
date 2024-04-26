
import pandas as pd
import seaborn as sns

# Load the sns_utils library
import seaborn.utils as utils

# Create a sample dataset
df = pd.DataFrame({
    "gender": ["male", "female"],
    "age": [20, 25, 30, 35],
    "salary": [50000, 60000, 70000, 80000]
})

# Create a scatterplot using seaborn
sns.scatterplot(x="age", y="salary", hue="gender", data=df)

# Add a linear regression line to the plot
sns.regplot(x="age", y="salary", hue="gender", data=df)

# Show the plot
sns.show()
