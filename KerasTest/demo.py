'''
Description: 
Author: aLittleMango
Date: 2021-07-26 14:41:55
LastEditTime: 2021-07-27 11:50:08
FilePath: \VSCode-Python\KerasTest\demo.py
'''

import tensorflow as tf
import numpy as np
import tensorflow as keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
 
# Generate dummy data
x_train = np.random.random((1000, 20))
y_train = np.random.randint(2, size=(1000, 1))
x_test = np.random.random((100, 20))
y_test = np.random.randint(2, size=(100, 1))
 
model = Sequential()
model.add(Dense(64, input_dim=20, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(1, activation="sigmoid"))
 
model.compile(loss="binary_crossentropy",
              optimizer="rmsprop",
              metrics=["accuracy"])
model.fit(x_train, y_train,
          epochs=20,
          batch_size=128)
score = model.evaluate(x_test, y_test, batch_size=128)
