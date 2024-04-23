
# Importing required libraries
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Creating a simple dataset (you can replace it with your own)
x = np.random.rand(100, 2)
y = np.random.randint(2, size=(100,))

# Preprocessing the input data using one-hot encoding for target variable 'y'
y_onehot = np.eye(3)[np.reshape(y, (-1,1))]

# Building a neural network model
model = Sequential()
model.add(Dense(12, activation='relu', input_shape=(x.shape[1],)))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='softmax'))

# Compiling the model
model.compile(loss='categorical_crossent', optimizer='adam', metrics=['accuracy'])

# Training the model for 10 epochs
history = model.fit(x, y_onehot, epochs=10)

# Printing the final evaluation results
scores = model.evaluate(x, y_onehot)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
