import keras
from keras.models import Sequential
from keras.layers import Dense

# Create a sequential model
model = Sequential()

# Add the first layer (dense layer with 128 units)
model.add(Dense(128, activation='relu', input_shape=(784,)))

# Add the second layer (dense layer with 64 units)
model.add(Dense(64, activation='sigmoid'))

# Add the output layer (dense layer with 10 units)
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model on the training data
model.fit(x_train, y_train, epochs=10, batch_size=32)

# Use the trained model to make predictions on the test data
predictions = model.predict(x_test)