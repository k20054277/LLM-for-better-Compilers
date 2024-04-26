
import keras
import numpy as np

# Define a simple linear regression model
model = keras.models.Sequential([
    keras.layers.Dense(10, activation='relu'),
    keras.layers.Dense(1, activation='linear')
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Generate some sample data
x_train = np.array([[1, 2], [3, 4], [5, 6]])
y_train = np.array([10, 12, 14])

# Fit the model
model.fit(x_train, y_train, epochs=10)

# Assert that the model is working
assert model.predict(x_train) == y_train

# Print the model's summary
model.summary()
