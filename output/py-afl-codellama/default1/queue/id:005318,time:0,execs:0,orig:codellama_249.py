import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Create a sequential model with one dense layer
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(10,)))

# Compile the model with a loss function and an optimizer
model.compile(loss='mean_squared_error', optimizer='adam')

# Train the model on some data
X = np.random.rand(100, 10)
y = np.random.rand(100, 64)
model.fit(X, y, epochs=10, batch_size=32)

# Evaluate the model on some test data
test_data = np.random.rand(50, 10)
test_labels = np.random.rand(50, 64)
test_loss = model.evaluate(test_data, test_labels, verbose=0)
print('Test loss:', test_loss)

# Use `False` to turn off the training loop
model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2, shuffle=True, class_weight=None, sample_weight=None, initial_epoch=0)