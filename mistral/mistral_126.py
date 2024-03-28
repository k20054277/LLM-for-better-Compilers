
# Import necessary libraries
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Create some sample data
x_train = np.random.rand(100, 2)
y_train = np.random.randint(2, size=(100,)) # ground truth labels (False for 0 and True for 1)

# Build a simple neural network model using Keras
model = Sequential()
model.add(Dense(32, activation='relu', input_shape=(2,))) # hidden layer with ReLU activation function
model.add(Dense(1, activation='sigmoid')) # output layer with sigmoid activation function

# Compile the model with a loss function and an optimizer
model.compile(loss='binary_crossent', optimizer='adam')

# Train the model on our sample data
model.fit(x_train, y_train, epochs=10, batch_size=32)

# Predict the output for a new input (False in this case)
input_sample = np.array([[0., False]]) # Note: The second value is represented as a NumPy boolean array (False), which is internally converted to 0 in Python
output = model.predict(input_sample)[0][0]

# Print the predicted output
print('Predicted output for input [0, False]: {}'.format(output))
