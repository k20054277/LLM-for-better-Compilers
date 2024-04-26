
import pandas as pd
import scikit_learn as sk

# Load the pandas and scikit-learn libraries

# Create a pandas DataFrame
df = pd.DataFrame({"Name": ["John Doe", "Jane Doe", "Peter Pan"], "Age": [25, 30, 12], "City": ["New York", "Los Angeles", "Neverland"]})

# Print the DataFrame
print(df)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(df.drop("Name", axis=1), df["Age"], test_size=0.2, random_state=42)

# Create a linear regression model
model = sk.linear_model.LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print the predictions
print(y_pred)
