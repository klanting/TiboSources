import tensorflow as tf
from tensorflow import keras
import numpy as np
import os
from cv2 import cv2
import math
from tensorflow.keras import datasets, layers, models, activations

classes = ["cat", "dog", "car"]


def Load_Images(path, resize=True, size=(160, 160)):
    images, labels = [], []

    """get images_ic from the directory"""
    for dirpath, dnames, fnames in os.walk(path):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".jpeg"):

                image = cv2.imread(f"{path}/{f}")

                """re-shape so it is all the same"""
                if resize:
                    image = cv2.resize(image, size, interpolation=cv2.INTER_LINEAR)
                images.append(image)

                for c in classes:
                    if c in f:
                        i = classes.index(c)
                        labels.append(i)

    images = np.stack(images, axis=0)

    labels = np.stack(labels, axis=0)
    return images, labels


def take_parts(images, sample=5):
    pictures = []
    pictures_mapping = []

    for image in images:

        for i in range(0, 160, sample):
            for j in range(0, 160, sample):

                """take different samples"""
                new_image = []
                for height in image:
                    new_image.append(height[0+i:160+i])
                new_image = new_image[0+j:160+j]
                pictures.append(new_image)
                pictures_mapping.append((i, j, 160+i, 160+j))

    pictures = np.stack(pictures, axis=0)

    return pictures, pictures_mapping


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
    model.add(layers.Dense(len(classes), activation='softmax'))

    print(model.summary())

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    """model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])"""

    model.fit(train_images, train_labels, epochs=10)

    return model

model = Train()
test_images, test_labels = Load_Images("input_od", True, (320, 320))
main_image = test_images[0]

print(test_images.shape)
test_images, test_mapping = take_parts(test_images)
print(test_images.shape)
test_images = test_images / 255.0

prediction = model.predict(np.array(test_images))
pre_max = 0
for i, p in enumerate(prediction):
    if max(p) > pre_max:
        pre_max = max(p)

#cap = pre_max * 0.8
cap = 0.8

maxi = 0
max_index = 0

for i, p in enumerate(prediction):
    print(p)
    print(max(p))

    """
    if max(p) > maxi:
        maxi = max(p)
        max_index = i
    """

    if max(p) > cap:
        item = np.where(p == max(p))[0]
        print(item)

        x1, y1, x2, y2 = test_mapping[i]
        if item == 0:
            cv2.rectangle(main_image, (x1, y1), (x2, y2), (0, 255, 255), 2)
        elif item == 1:
            cv2.rectangle(main_image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        elif item == 2:
            cv2.rectangle(main_image, (x1, y1), (x2, y2), (0, 0, 255), 2)


#print(max_index)
#print(maxi)

"""
x1, y1, x2, y2 = test_mapping[max_index]
cv2.rectangle(main_image, (x1, y1), (x2, y2), (255, 0, 0), 2)
"""

cv2.imshow('image', main_image)
cv2.waitKey(0)
