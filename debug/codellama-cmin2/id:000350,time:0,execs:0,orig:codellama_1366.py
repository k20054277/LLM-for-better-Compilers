import seaborn as sns

# Load some data to visualize
tips = sns.load_dataset('tips')

# Create a bar plot of the average tip amount by day
sns.barplot(x='day', y='mean', data=tips)

# Use assert to check that the plot is as expected
assert sns.countplot(x='day', data=tips).equals(sns.barplot(x='day', y='mean', data=tips))