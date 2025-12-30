import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model

# Load Model (Cached so it only loads once)
@st.cache_resource
def get_model():
    # Path relative to project root as seen in your structure
    model_path = os.path.join('models', 'rps_model_v1.keras')
    return load_model(model_path)

model = get_model()
labels = ['Paper', 'Rock', 'Scissors']

class VideoProcessor(VideoTransformerBase):
    def transform(self, frame):
        # Convert the WebRTC frame to an OpenCV BGR image
        img = frame.to_ndarray(format="bgr24")

        # Preprocessing (Mirroring your OpenCV logic)
        # Defining a central ROI for the user to put their hand
        h, w, _ = img.shape
        roi = img[h//4:3*h//4, w//4:3*w//4]
        
        # Convert BGR to RGB for the model
        img_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
        img_resized = cv2.resize(img_rgb, (150, 150))
        img_normalized = img_resized / 255.0
        img_batch = np.expand_dims(img_normalized, axis=0)

        # Predict
        prediction = model.predict(img_batch, verbose=0)
        class_idx = np.argmax(prediction)
        confidence = np.max(prediction)

        # Annotate the original frame
        label_text = f"{labels[class_idx]}: {confidence*100:.1f}%"
        cv2.rectangle(img, (w//4, h//4), (3*w//4, 3*h//4), (0, 255, 0), 2)
        cv2.putText(img, label_text, (w//4, h//4 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        return img

# Streamlit UI
st.title("🖐️ Real-Time Rock Paper Scissors")
st.write("Position your hand inside the green box.")

webrtc_streamer(key="rps-filter", video_transformer_factory=VideoProcessor)