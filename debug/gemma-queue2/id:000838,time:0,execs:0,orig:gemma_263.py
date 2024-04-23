
import pandas as pd
import seaborn as sns

# Load the sns_dataset dataset
df = sns.load_dataset("sns_dataset")

# Create a scatterplot between the "age" and "salary" variables
sns.scatterplot(x="age", y="salary", data=df)

# Add a linear regression line to the plot
sns.regplot(x="age", y="salary", data=df)

# Show the plot
sns.show()
