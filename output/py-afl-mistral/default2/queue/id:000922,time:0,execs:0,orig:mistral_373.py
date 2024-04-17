
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Using None as a value in Python
data = {}
data['name'] = ['John', 'Jane', 'Mike', None]
data['age'] = [25, 30, np.nan, 45]

print("Data:")
print(data)

# Using Seaborn library for data visualization
np.random.seed(123)
x = np.random.randn(100)
y = np.where(np.isnan(x), None, x**2)

sns.scatterplot(x, y)
plt.title("Scatterplot with None values")
plt.show()

# Handle None values in seaborn plot
sns.boxplot(data=data, x='name', y='age')
plt.title("Boxplot handling None values")
plt.show()
