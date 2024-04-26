from keras.models import Sequential
from keras.layers import Dense, Dropout

# define model
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(10,)))
model.add(Dropout(0.5))
model.add(Dense(64, activation='softmax'))

# compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# train model
model.fit(X_train, y_train, epochs=10, batch_size=32)