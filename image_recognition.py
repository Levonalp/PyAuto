import numpy as np
import tensorflow as tf
from PIL import Image

def load_model_and_labels():
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    labels_path = tf.keras.utils.get_file(
        'ImageNetLabels.txt',
        'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
    with open(labels_path) as file:
        labels = file.read().splitlines()[1:]
    return model, labels

def preprocess_image(image_path):
    image = Image.open(image_path).resize((224, 224))
    image_array = np.array(image) / 255.0
    image_batch = np.expand_dims(image_array, axis=0)
    return image_batch

def recognize_image(model, labels, image_path):
    image_batch = preprocess_image(image_path)
    predictions = model.predict(image_batch)
    top_prediction = np.argmax(predictions[0])
    label = labels[top_prediction]
    confidence = round(predictions[0][top_prediction] * 100, 2)
    return label, confidence

# Load the model and labels
model, labels = load_model_and_labels()

# Image path
image_path = 'path/to/your/image.jpg'

# Perform image recognition
label, confidence = recognize_image(model, labels, image_path)
print(f"Recognized object: {label}")
print(f"Confidence: {confidence}%")

