import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Get the directory where 03_real_time.py is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Go up one level to the project root, then into models
model_path = os.path.join(script_dir, '..', 'models', 'rps_model_v1.keras')
model = load_model(model_path)

# Ensure labels match the alphabetical order Keras uses
labels = ['Paper', 'Rock', 'Scissors']

# Setup Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break

    # Preprocessing (Must match your training steps!)
    # Define a 'Region of Interest' (the box where you put your hand)
    roi = frame[100:400, 100:400]
    # IMPORTANT: Convert BGR (OpenCV default) to RGB (Model default)
    img_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    # Resize to the input shape your model expects
    img_resized = cv2.resize(img_rgb, (150, 150))
    # Normalize and add batch dimension
    img_normalized = img_resized / 255.0
    img_batch = np.expand_dims(img_normalized, axis=0)

    # Predict
    # verbose=0 stops the terminal from flooding with progress bars
    prediction = model.predict(img_batch, verbose=0)
    class_idx = np.argmax(prediction)
    confidence = np.max(prediction)

    # Display Results
    color = (0, 255, 0) # Green for the box
    label_text = f"{labels[class_idx]}: {confidence*100:.1f}%"
    
    # Draw the ROI box and the prediction text
    cv2.rectangle(frame, (100, 100), (400, 400), color, 2)
    cv2.putText(frame, label_text, (100, 85), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    
    cv2.imshow('RPS Real-Time Classifier', frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()