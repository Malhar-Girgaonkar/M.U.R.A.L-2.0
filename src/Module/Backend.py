import os
import shutil
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
import numpy as np
from PIL import Image

def Load_trained_model():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_dir, '..', 'Models', 'AI_vs_Human_model.h5')
        model_computed = load_model(model_path)
        print(f"Model loaded successfully from {model_path}")
        return model_computed
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def preprocess(image_path):
    try:
        img_height, img_width = 256, 256
        image_loaded = image.load_img(image_path, target_size=(img_height, img_width))
        image_array = image.img_to_array(image_loaded)
        img_array = np.expand_dims(image_array, axis=0)
        img_array /= 255.0
        return img_array
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        return None

def Predictions(img_path):
    model_computed = Load_trained_model()
    if model_computed is None:
        return "Model loading error"
    #preprocess data
    img_array = preprocess(img_path)
    if img_array is None:
        return "Image preprocessing error"
    #predict with model_computed
    try:
        prediction = model_computed.predict(img_array)
    except Exception as e:
        print(f"Error during prediction: {e}")
        return "Prediction error"
    #set threshold
    threshold = 0.5
    #print(prediction)
    if prediction[0][0] > threshold:
        return("AI Generated art")
    else:
        return("Human generated art")

def Get_image_info(image_path):
    #open image as img
    img = Image.open(image_path)
    #extract image EXIF data
    exif_data = img._getexif()
    #check if exif_data is none and if not print it
    if exif_data is not None:
        dict_info = dict()
        for tag, value in exif_data.items():
            tag_name = Image.ExifTags.TAGS.get(tag, tag)
            dict_info[tag_name] = value
            #print(f"{tag_name}: {value}")
        return(dict_info)
    return {"Info": "No EXIF data found"}