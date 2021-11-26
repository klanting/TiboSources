import tensorflow as tf
from tensorflow import keras
import numpy as np
import os
from cv2 import cv2
import math


def Load_Images(path):
    images, gray_images = [], []

    """get images_ic from the directory"""
    for dirpath, dnames, fnames in os.walk(path):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):

                image = cv2.imread(f"{path}/{f}")

                """re-shape so it is all the same"""
                image = cv2.resize(image, (1000, 1000), interpolation=cv2.INTER_LINEAR)

                gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

                images.append(image)
                gray_images.append(gray_image)

    images = np.stack(images, axis=0)
    gray_images = np.stack(gray_images, axis=0)
    print(images[0])

    return gray_images, images


def Train():

    train_images, train_labels = Load_Images("images_ic")

    print(train_images.shape)
    print(train_labels.shape)

    train_images = train_images / 255.0

    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(1000, 1000)),  # input_ic layer (1)
        keras.layers.Dense(128, activation='relu'),  # hidden layer (2)
        keras.layers.Dense(1000000, activation='relu'),
        keras.layers.Reshape((1000, 1000)) # output layer (3)
    ])
    print(model.output_shape)
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=10)  # we pass the data, labels and epochs and watch the magic!
    return model


model = Train()
test_images, test_labels = Load_Images("input_ic")

test_images = test_images / 255.0

predictions = model.predict(test_images)
print(predictions.shape)

predictions = np.round(predictions * 255.0)
print(predictions[0])
cv2.imshow('image', predictions[0])
cv2.waitKey(0)
