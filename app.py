import streamlit as st
import numpy as np
from PIL import Image
from keras.models import load_model
import os

st.set_page_config(page_title="Traffic Sign Classifier", page_icon="🚦")

st.title("🚦 Traffic Sign Classification")
st.write("Upload an image of a traffic sign to see what it means.")

@st.cache_resource
def load_keras_model():
    model_path = 'traffic_classifier.h5'
    if os.path.exists(model_path):
        return load_model(model_path, compile=False)
    return None

model = load_keras_model()

if model is None:
    st.error("Model not found. Please ensure `traffic_classifier.h5` is in the same directory.")

classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)', 
            3:'Speed limit (50km/h)', 
            4:'Speed limit (60km/h)', 
            5:'Speed limit (70km/h)', 
            6:'Speed limit (80km/h)', 
            7:'End of speed limit (80km/h)', 
            8:'Speed limit (100km/h)', 
            9:'Speed limit (120km/h)', 
            10:'No passing', 
            11:'No passing veh over 3.5 tons', 
            12:'Right-of-way at intersection', 
            13:'Priority road', 
            14:'Yield', 
            15:'Stop', 
            16:'No vehicles', 
            17:'Veh > 3.5 tons prohibited', 
            18:'No entry', 
            19:'General caution', 
            20:'Dangerous curve left', 
            21:'Dangerous curve right', 
            22:'Double curve', 
            23:'Bumpy road', 
            24:'Slippery road', 
            25:'Road narrows on the right', 
            26:'Road work', 
            27:'Traffic signals', 
            28:'Pedestrians', 
            29:'Children crossing', 
            30:'Bicycles crossing', 
            31:'Beware of ice/snow',
            32:'Wild animals crossing', 
            33:'End speed + passing limits', 
            34:'Turn right ahead', 
            35:'Turn left ahead', 
            36:'Ahead only', 
            37:'Go straight or right', 
            38:'Go straight or left', 
            39:'Keep right', 
            40:'Keep left', 
            41:'Roundabout mandatory', 
            42:'End of no passing', 
            43:'End no passing veh > 3.5 tons' }

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg", "webp"])

if uploaded_file is not None and model is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', width=300)
    
    # Resize and preprocess the image just like in the Tkinter app
    img = image.resize((30,30))
    img = np.expand_dims(img, axis=0)
    img = np.array(img)
    
    # Predict
    pred = np.argmax(model.predict(img), axis=-1)[0]
    sign_name = classes[pred + 1]
    
    st.success(f"**Sign:** {sign_name}")
