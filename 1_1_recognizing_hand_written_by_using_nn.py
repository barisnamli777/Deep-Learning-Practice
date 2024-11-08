# -*- coding: utf-8 -*-
"""1.1_Recognizing_Hand_Written_by_Using_NN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G6TjucqumEWqnAaEXY6aYyU81R7PhIg5

In this study, handwriting is recognized with NN. For this, the mnist dataset and more than one layer was used.
"""
# İmporting the libraries
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Loading datasets as mnist
mnist=keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test)=mnist.load_data()

# Printing the shape of the X and Y values
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

# Reshape the X_train and X_test
X_train=X_train.reshape(X_train.shape[0],28*28)
X_test=X_test.reshape(X_test.shape[0],28*28)
print(X_train.shape)
print(X_test.shape)

#Normalizing X_train and X_test
X_train=X_train/255
X_test=X_test/255

X_train=X_train.astype("float32")
X_test=X_test.astype("float32")

Y_train=keras.utils.to_categorical(Y_train,10)
Y_test=keras.utils.to_categorical(Y_test,10)

model=keras.models.Sequential()
model.add(keras.layers.Dense(128,
                             input_shape=(784,),
                             name="dense_layer_1",
                             activation="relu"))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(128,
                             name="dense_layer_2",
                             activation="relu"))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(10,
                             name="dense_layer_3",
                             activation="softmax"))

model.summary()

model.compile(optimizer="SGD",
              loss="categorical_crossentropy",
              metrics=["accuracy"])

model.fit(X_train, Y_train, epochs=200, batch_size=128, verbose=1, validation_split=0.2)

test_loss, test_acc=model.evaluate(X_test, Y_test)
print("Test accuracy is:", test_acc)
