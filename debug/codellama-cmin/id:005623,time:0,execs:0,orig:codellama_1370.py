# Import necessary libraries
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import numpy as np

# Load the Boston Housing dataset
boston = datasets.load_boston()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)

# Create a LinearRegression object
lr = LinearRegression()

# Train the model on the training data
lr.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = lr.predict(X_test)

# Evaluate the performance of the model using mean squared error
mse = np.mean((y_pred - y_test) ** 2)
print("Mean Squared Error:", mse)

# Use assert to check if the mean squared error is less than a certain value
assert mse <