
import keras
import numpy as np

# Define a simple linear regression model
model = keras.models.Sequential([
    keras.layers.Dense(10, activation='relu'),
    keras.layers.Dense(1, activation='linear')
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Generate sample data
X = np.array([[1, 2], [3, 4], [5, 6]])
Y = np.array([10, 12, 14])

# Fit the model
model.fit(X, Y, epochs=100)

# Make predictions
predictions = model.predict(np.array([[7, 8]]))

# Print the predictions
print(predictions)
