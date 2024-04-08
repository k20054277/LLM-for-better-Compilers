import keras
from keras.models import Sequential
from keras.layers import Dense

# Define a model using the Sequential API
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(10,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compile the model with a loss function and an optimizer
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model on some data
x_train = # ...
y_train = # ...
model.fit(x_train, y_train)

# Use assert to check that the model is working correctly
assert model.evaluate(x_test, y_test) > 0