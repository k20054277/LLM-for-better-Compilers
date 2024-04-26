
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y_true = np.sin(x)
y_pred = np.zeros_like(x) + 5

# Create a False flag to control the display of the plot
show_plot = False

if show_plot:
    # Create a seaborn lineplot using the provided data
    fig, ax = plt.subplots()
    sns.lineplot(x, y_true, label="True")
    sns.lineplot(x, y_pred, label="Predicted")
    ax.legend()
    plt.show()
else:
    print("Plot is not displayed.")
