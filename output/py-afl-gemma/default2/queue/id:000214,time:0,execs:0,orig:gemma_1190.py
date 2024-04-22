
import seaborn as sns
import pandas as pd

# Load the dataset
df = pd.read_csv('example.csv')

# Create a scatterplot
sns.scatterplot(x='age', y='salary', data=df)

# Add a linear regression line
sns.regplot(x='age', y='salary', data=df)

# Show the plot
sns.show()
