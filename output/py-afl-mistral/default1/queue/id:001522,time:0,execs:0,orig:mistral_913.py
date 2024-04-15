
# Importing necessary libraries
import numpy as np
from sklearn import datasets, model_selection

# Generating a random dataset as an example
X = np.random.rand(100, 4)
y = np.random.randint(2, size=100)

# Creating a mask for demonstrating the logical 'and' operator
mask = (X[:, 0] > 0.5) and (X[:, 1] < 0.3)
print("Mask:")
print(mask)

# Applying this mask to X and y for filtering the data
X_filtered = X[np.where(mask)]
y_filtered = y[np.where(mask)]
print("Filtered Data:")
print(np.concatenate((X_filtered, np.ones((len(X_filtered), 1)) * y_filtered), axis=1))

# Applying Scikit-Learn for logical data processing and machine learning
# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=42)

# Creating a custom boolean feature for demonstration
X_train['feature_boolean'] = (X_train[:, 1] > 0.4) & (X_train[:, 2] < 0.6)
X_test['feature_boolean'] = (X_test[:, 1] > 0.4) & (X_test[:, 2] < 0.6)

# Creating a decision tree classifier using the custom boolean feature
clf = model_selection.DecisionTreeClassifier()
clf.fit(X_train[['feature_boolean']], y_train)

# Predicting on test data using the trained classifier
y_pred = clf.predict(X_test[['feature_boolean']])
print("Predictions:")
print(np.concatenate((X_test[['feature_boolean']], np.ones((len(X_test), 1)) * y_pred), axis=1))
