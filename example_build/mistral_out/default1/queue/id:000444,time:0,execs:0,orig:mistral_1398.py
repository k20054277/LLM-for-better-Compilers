
import numpy as np
import seaborn as sns
import assertpy as assertp

# Create a simple dataset using NumPy
data = np.random.rand(10, 2)
labels = np.random.randint(low=0, high=3, size=10)

# Test the shape of data using Assert
def test_shape():
    assertp.assert_that(data.shape).is_equal_to((10, 2))

test_shape()

# Visualize the data using Seaborn
sns.scatterplot(x=data[:, 0], y=data[:, 1], hue=labels)
sns.despine(offset=30, trunc=True)
