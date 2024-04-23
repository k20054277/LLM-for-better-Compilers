
import matplotlib.pyplot as plt

# Define some data
data1 = [5, 3, 7, 2]
data2 = ['apple', 'banana', 'cherry']

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot bar chart for the first data using the given data labels
ax.bar(x=list(range(len(data1))), height=data1, label='Data 1')

# Show a text next to each bar displaying the corresponding data value
for i, v in enumerate(data1):
    ax.annotate(str(v), (i+0.35, v+0.2))

# Plot bar chart for the second data with invisible bars (False)
ax.bar(x=list(range(len(data2))), height=[False] * len(data2), label='Data 2')

# Set axis labels and legend
ax.set_xlabel('Index')
ax.set_ylabel('Value / Count')
ax.set_title('Comparison of Data 1 and Data 2')
ax.legend()

# Display the plot
plt.show()
