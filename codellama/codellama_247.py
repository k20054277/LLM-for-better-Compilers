import seaborn as sns

# create a dataset
data = {'x': [1, 2, 3], 'y': [4, 5, 6]}

# create a figure and axis object
fig, ax = plt.subplots()

# plot the data with seaborn
sns.scatterplot(x='x', y='y', data=data, ax=ax)

# set the title of the plot
plt.title('My Plot')

# set the x-axis label
plt.xlabel('X Axis Label')

# set the y-axis label
plt.ylabel('Y Axis Label')

# add a legend to the plot
ax.legend()

# show the plot
plt.show()