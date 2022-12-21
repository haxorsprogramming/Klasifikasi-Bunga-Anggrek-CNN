from tensorflow import keras

import tensorflow as tf
import numpy as np

data_model = "static/model"

batch_size = 32
size = 180

def testingDataUji(className, kdPengujian):

    class_names = ["Dendrobium_Dindii", "Dendrobium_Startiotes", "Dendrobium_Taurinum"]
    num_classes = len(class_names)
    print(class_names)
    model = keras.models.load_model(data_model)

    img_pred_dir = "static/upload_data_uji/"+str(kdPengujian)+".png"

    img_pred = keras.preprocessing.image.load_img(
        img_pred_dir, target_size=(size, size)
    )

    img_pred_array = keras.preprocessing.image.img_to_array(img_pred)
    img_pred_array = tf.expand_dims(img_pred_array, 0)

    prediction = model.predict(img_pred_array)
    score = tf.nn.softmax(prediction[0])

    print(
        "This image most likely belongs to {} with a {:.2f} percent confidence."
        .format(class_names[np.argmax(score)], 100 * np.max(score))
    )

    dr = {
        'confidence' : 100 * np.max(score),
        'class' : class_names[np.argmax(score)]
    }

    return dr
