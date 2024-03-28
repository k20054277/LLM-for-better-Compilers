
# Import necessary libraries
import numpy as np
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression

# Create a boolean dataset using NumPy
data = np.array([[True, True], [False, False], [True, True], [False, False]])
labels = np.array([1, 1, 1, 0])

# Split the dataset into training and testing sets using Scikit-Learn's model_selection module
X_train, X_test, y_train, y_test = model_selection.train_test_split(data, labels, test_size=0.3, random_state=42)

# Create and fit a logistic regression model using Scikit-Learn's LogisticRegression class
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test dataset
predictions = model.predict(X_test)

# Print some information about the trained model and its performance
print("Model coefficients:")
print(model.coef_)
print("\nIntercept:")
print(model.intercept_)
print("\nTest set predictions:")
print(predictions)
print("\nTest set true labels:")
print(y_test)
print("\nTest set accuracy:")
print(np.mean(predictions == y_test))
