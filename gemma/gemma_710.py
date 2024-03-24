
import scikit_learn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Import True and False
import numpy as np
True_or_False = np.array([True, False])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(True_or_False, True_or_False, test_size=0.2, random_state=42)

# Create and fit a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print the results
print("The accuracy of the model is:", scikit_learn.metrics.accuracy_score(y_test, y_pred))
