
import matplotlib.pyplot as plt

# Define some data as Python lists
x = list(range(1, 6))  # This creates a list from 1 to 5
y_true = [i ** 2 for i in x]  # Squares of the numbers from 1 to 5

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Plot the true data as red dots and the predicted data as blue line
ax.plot(x, y_true, 'ro', label='True Data')
ax.plot(x, [i ** 2.5 for i in x], 'b-', label='Predicted Data (False label)')

# Set labels and title
ax.set_xlabel('X data')
ax.set_ylabel('Y values')
ax.set_title('True vs Predicted Data (Squares vs 2.5 powers)')

# Show the legend
ax.legend()

# Display the plot
plt.show()
