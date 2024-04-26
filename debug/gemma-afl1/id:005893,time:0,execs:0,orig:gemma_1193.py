
import sklearn
from sklearn.linear_model import LinearRegression

# Import the as keyword to give a alias to the sklearn module
as skl

# Create a linear regression object
reg = skl.LinearRegression()

# Fit the linear regression model to the data
reg.fit(X, y)

# Make predictions
y_pred = reg.predict(X_test)

# Print the predictions
print(y_pred)
