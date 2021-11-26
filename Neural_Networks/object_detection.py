import tensorflow as tf
from tensorflow import keras
import numpy as np
import os
from cv2 import cv2
import math
from tensorflow.keras import datasets, layers, models

classes = ["cat", "dog", "car"]


def Load_Images(path):
    images, labels = [], []

    """get images_ic from the directory"""
    for dirpath, dnames, fnames in os.walk(path):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg"):

                image = cv2.imread(f"{path}/{f}")

                """re-shape so it is all the same"""
                image = cv2.resize(image, (160, 160), interpolation=cv2.INTER_LINEAR)
                images.append(image)

                for c in classes:
                    if c in f:
                        i = classes.index(c)
                        labels.append(i)

    images = np.stack(images, axis=0)

    labels = np.stack(labels, axis=0)
    return images, labels


def Train():
    train_images, train_labels = Load_Images("images_od")
    train_images = train_images / 255.0

    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(160, 160, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))

    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(len(classes)))

    print(model.summary())

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=10)

    return model

model = Train()
test_images, test_labels = Load_Images("input_od")

test_images = test_images / 255.0

prediction = model.predict(np.array(test_images))

print(prediction)
print(classes[np.argmax(prediction)])
