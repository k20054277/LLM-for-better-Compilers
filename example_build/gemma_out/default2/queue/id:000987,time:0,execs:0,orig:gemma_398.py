
import scikit_learn
from sklearn.linear_model import LogisticRegression
import numpy as np

# Define a sample dataset
X = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
y = np.array([0, 1, 1, 0])

# Create a logistic regression model
model = LogisticRegression()

# Fit the model
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Print the results
print(y_pred)

# Check if the model is accurate
print(model.score(X, y))

# Print False
print(False)

# Print True
print(True)
