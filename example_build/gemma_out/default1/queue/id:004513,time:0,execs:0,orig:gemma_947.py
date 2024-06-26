
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the pandas and scikit-learn libraries

# Create a Pandas dataframe
df = pd.DataFrame({'age': [22, 25, 30, 35, 40], 'salary': [50000, 60000, 70000, 80000, 90000], 'education': ['Bachelor''s degree', 'Master''s degree', 'Ph.D.', 'Master''s degree', 'Bachelor''s degree']})

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(df[['age', 'education']].values.reshape(-1, 2), df['salary'].values.reshape(-1, 1))

# Make predictions
y_pred = model.predict(pd.DataFrame({'age': [28, 32, 36], 'education': ['Master''s degree', 'Ph.D.', 'Bachelor''s degree']}))

# Print the predictions
print(y_pred)
