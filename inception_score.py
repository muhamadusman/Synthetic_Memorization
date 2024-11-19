import os
import numpy as np
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
from tensorflow.keras.preprocessing import image
from scipy.stats import entropy

def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        img = image.load_img(img_path, target_size=(299, 299))
        img_array = image.img_to_array(img)
        images.append(img_array)
    return np.array(images)

def inception_score(predictions):
    p_y = np.mean(predictions, axis=0)
    e = predictions * (np.log(predictions) - np.log(p_y))
    e_sum = np.sum(e, axis=1)
    score = np.exp(np.mean(e_sum))
    return score

def calculate_inception_score(folder1, folder2):
    images1 = load_images(folder1)
    images2 = load_images(folder2)

    all_images = np.concatenate((images1, images2), axis=0)
    all_images = preprocess_input(all_images)

    model = InceptionV3(include_top=True, weights='imagenet', input_shape=(299, 299, 3), classes=1000)

    predictions = model.predict(all_images)
    score = inception_score(predictions)

    return score

folder1 = path to first folder 
folder2 = path to second folder

score = calculate_inception_score(folder1, folder2)
print(f"Inception Score: {score}")
