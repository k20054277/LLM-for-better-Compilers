import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
rfc = RandomForestClassifier(n_estimators=10, random_state=42)

# Train the model on the training data
rfc.fit(X_train, y_train)

# Predict on the test data
predictions = rfc.predict(X_test)

# Evaluate the model using accuracy score
accuracy = rfc.score(X_test, y_test)
print("Accuracy:", accuracy)