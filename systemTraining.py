from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import uuid

import os
import pathlib
import tensorflow as tf
import matplotlib.pyplot as plt


# section untuk training data 
data_model = "static/model"
dataset_dir = "static/dataset"
data_dir = pathlib.Path(dataset_dir)

batch_size = 32
size = 180

def trainingProcess(kdPengujian):
    print(" ========== training start ==========")
    # set training data 
    train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=123,
        image_size=(size, size),
        batch_size=batch_size
    )
    # set testing data 
    val_dataset = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=123,
        image_size=(size, size),
        batch_size=batch_size
    )
    # tuning dataset 
    class_names = train_dataset.class_names
    AUTOTUNE = tf.data.AUTOTUNE
    train_dataset = train_dataset.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_dataset = val_dataset.cache().prefetch(buffer_size=AUTOTUNE)
    normalization_layer = layers.experimental.preprocessing.Rescaling(1./255)
    normalized_dataset = train_dataset.map(lambda x, y: (normalization_layer(x), y))
    image_batch, labels_batch = next(iter(normalized_dataset))
    first_image = image_batch[0]
    num_classes = len(class_names)
    # build model 
    model = Sequential([
        layers.experimental.preprocessing.Rescaling(1./255, input_shape=(size, size, 3)),
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes)    
    ])
    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy']
    )
    model.summary()
    # start iteration 
    epochs = 10
    history = model.fit(train_dataset,validation_data=val_dataset,epochs=epochs)
    # create plot eval
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs_range = range(epochs)
    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')
    # Grafik training and validation loss (save file plot)
    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.savefig('static/file_plot/train_eval/'+str(kdPengujian)+'.png')
    # data augmentation
    data_augmentation = keras.Sequential(
        [
            layers.experimental.preprocessing.RandomFlip("horizontal",input_shape = (size,size,3)),
            layers.experimental.preprocessing.RandomRotation(0.1),
            layers.experimental.preprocessing.RandomZoom(0.1),
        ]
    )
    # model sequental
    model = Sequential([
        data_augmentation,
        layers.experimental.preprocessing.Rescaling(1./255),
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Dropout(0.25),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes)
    ])
    model.compile(
        optimizer='adam',
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy']
    )
    # epoech sequental 2
    model.summary()
    epochs = 15
    history = model.fit(train_dataset,validation_data=val_dataset,epochs=epochs)
    # accuracy evaluasi
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs_range = range(epochs)
    plt.figure(figsize=(8, 8))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, acc, label='Training Accuracy')
    plt.plot(epochs_range, val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')
    #Grafik training and validation loss
    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.savefig('static/file_plot/acc_evaluasi/'+str(kdPengujian)+'.png')
    # save model 
    if not os.path.exists(data_model):
        os.makedirs(data_model)
    model.save(data_model, overwrite=True)
    print("model berhasil di simpan")

    print(" ========== training finish ==========")
    return 0