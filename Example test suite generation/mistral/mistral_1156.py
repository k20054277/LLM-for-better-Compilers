
# Importing necessary libraries
import numpy as np
from sklearn.decomposition import PCA

# Creating a random dataset
data = np.random.rand(100, 5) # Generating a random data of shape (100 samples, 5 features)

# Using scikit-learn's PCA for dimensionality reduction
pca = PCA(n_components=3) # Reducing dimensions to 3
X_reduced = pca.fit_transform(data) # Fitting PCA on data and reducing the dimensions

# Assigning the name 'X' to the reduced data for simplicity
X = X_reduced

# Printing the explained variance ratio of each principal component
print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)

# Using 'as' keyword for renaming the components of the reduced data
PC1, PC2, PC3 = X.T # Transposing the matrix to get the components as separate arrays

# Printing the mean and standard deviation of each principal component
print("\nMean:")
print(np.mean(X, axis=0))
print("Standard Deviation:")
print(np.std(X, axis=0))

# Using 'as' keyword for assigning names to the principal components
PC1_mean, PC2_mean, PC3_mean = np.mean(X, axis=0) as mean_values, \
                              np.std(X, axis=0) as std_values

# Printing the mean and standard deviation using 'as' keyword
print("\nMean:")
print(mean_values)
print("Standard Deviation:")
print(std_values)
