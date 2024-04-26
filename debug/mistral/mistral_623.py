
# Importing necessary libraries
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Generate some random data for demonstration purposes
X = np.random.randn(100, 2) # 100 samples with 2 features each
y = np.rint(np.random.normal(size=100), 1) # 100 samples with binary labels (0 or 1)

# Define a simple feedforward neural network model
model = Sequential()
model.add(Dense(32, input_shape=(X.shape[1],), activation='relu')) # Hidden layer with 32 neurons and ReLU activation
model.add(Dense(1, activation='sigmoid')) # Output layer with sigmoid activation for binary classification

# Compile the model with a loss function and an optimizer
model.compile(loss='binary_crossent', optimizer='adam', metrics=['accuracy'])

# Train the model on our data
history = model.fit(X, y, epochs=100, batch_size=32, verbose=0)

# Now let's create some new data and make predictions
new_data = np.array([[True, True], [False, False]]) # New data with 2 binary features
predictions = model.predict(new_data) # Make predictions using our trained model
print("Predictions for new data: ", predictions) # Print the predictions
