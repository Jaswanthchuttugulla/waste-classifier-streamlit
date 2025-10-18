import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load your model
model = load_model('waste_classifier_model.h5')

# List your class names in the correct order!
class_labels = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

def predict(img):
    img = img.resize((128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)[0]
    return class_labels[predicted_class]

st.title('Waste Classifier')
st.write('Upload a waste image to classify.')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)
    st.write("Classifying...")
    label = predict(img)
    st.success(f"Predicted class: {label}")
